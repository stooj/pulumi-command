// Copyright 2016-2022, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//	http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package util

import (
	"bufio"
	"io"
	"sync"

	p "github.com/pulumi/pulumi-go-provider"
	"github.com/pulumi/pulumi/sdk/v3/go/common/diag"
)

const PULUMI_COMMAND_STDOUT = "PULUMI_COMMAND_STDOUT"
const PULUMI_COMMAND_STDERR = "PULUMI_COMMAND_STDERR"

func CopyOutput(ctx p.Context, r io.Reader, doneCh chan<- struct{}, severity diag.Severity) {
	defer close(doneCh)
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		ctx.LogStatus(severity, scanner.Text())
	}
}

type ConcurrentWriter struct {
	Writer io.Writer
	mu     sync.Mutex
}

func (w *ConcurrentWriter) Write(bs []byte) (int, error) {
	w.mu.Lock()
	defer w.mu.Unlock()
	return w.Writer.Write(bs)
}
