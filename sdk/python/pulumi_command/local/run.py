# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'RunResult',
    'AwaitableRunResult',
    'run',
    'run_output',
]

@pulumi.output_type
class RunResult:
    def __init__(__self__, archive=None, archive_paths=None, asset_paths=None, assets=None, command=None, dir=None, environment=None, interpreter=None, stderr=None, stdin=None, stdout=None):
        if archive and not isinstance(archive, pulumi.Archive):
            raise TypeError("Expected argument 'archive' to be a pulumi.Archive")
        pulumi.set(__self__, "archive", archive)
        if archive_paths and not isinstance(archive_paths, list):
            raise TypeError("Expected argument 'archive_paths' to be a list")
        pulumi.set(__self__, "archive_paths", archive_paths)
        if asset_paths and not isinstance(asset_paths, list):
            raise TypeError("Expected argument 'asset_paths' to be a list")
        pulumi.set(__self__, "asset_paths", asset_paths)
        if assets and not isinstance(assets, dict):
            raise TypeError("Expected argument 'assets' to be a dict")
        pulumi.set(__self__, "assets", assets)
        if command and not isinstance(command, str):
            raise TypeError("Expected argument 'command' to be a str")
        pulumi.set(__self__, "command", command)
        if dir and not isinstance(dir, str):
            raise TypeError("Expected argument 'dir' to be a str")
        pulumi.set(__self__, "dir", dir)
        if environment and not isinstance(environment, dict):
            raise TypeError("Expected argument 'environment' to be a dict")
        pulumi.set(__self__, "environment", environment)
        if interpreter and not isinstance(interpreter, list):
            raise TypeError("Expected argument 'interpreter' to be a list")
        pulumi.set(__self__, "interpreter", interpreter)
        if stderr and not isinstance(stderr, str):
            raise TypeError("Expected argument 'stderr' to be a str")
        pulumi.set(__self__, "stderr", stderr)
        if stdin and not isinstance(stdin, str):
            raise TypeError("Expected argument 'stdin' to be a str")
        pulumi.set(__self__, "stdin", stdin)
        if stdout and not isinstance(stdout, str):
            raise TypeError("Expected argument 'stdout' to be a str")
        pulumi.set(__self__, "stdout", stdout)

    @property
    @pulumi.getter
    def archive(self) -> Optional[pulumi.Archive]:
        """
        An archive asset containing files found after running the command.
        """
        return pulumi.get(self, "archive")

    @property
    @pulumi.getter(name="archivePaths")
    def archive_paths(self) -> Optional[Sequence[str]]:
        """
        A list of path globs to return as a single archive asset after the command completes.

        When specifying glob patterns the following rules apply:
        - We only include files not directories for assets and archives.
        - Path separators are `/` on all platforms - including Windows.
        - Patterns starting with `!` are 'exclude' rules.
        - Rules are evaluated in order, so exclude rules should be after inclusion rules.
        - `*` matches anything except `/`
        - `**` matches anything, _including_ `/`
        - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
        - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)

        #### Example

        Given the rules:
        ```yaml
        - "assets/**"
        - "src/**.js"
        - "!**secret.*"
        ```

        When evaluating against this folder:

        ```yaml
        - assets/
          - logos/
            - logo.svg
        - src/
          - index.js
          - secret.js
        ```

        The following paths will be returned:

        ```yaml
        - assets/logos/logo.svg
        - src/index.js
        ```
        """
        return pulumi.get(self, "archive_paths")

    @property
    @pulumi.getter(name="assetPaths")
    def asset_paths(self) -> Optional[Sequence[str]]:
        """
        A list of path globs to read after the command completes.

        When specifying glob patterns the following rules apply:
        - We only include files not directories for assets and archives.
        - Path separators are `/` on all platforms - including Windows.
        - Patterns starting with `!` are 'exclude' rules.
        - Rules are evaluated in order, so exclude rules should be after inclusion rules.
        - `*` matches anything except `/`
        - `**` matches anything, _including_ `/`
        - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
        - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)

        #### Example

        Given the rules:
        ```yaml
        - "assets/**"
        - "src/**.js"
        - "!**secret.*"
        ```

        When evaluating against this folder:

        ```yaml
        - assets/
          - logos/
            - logo.svg
        - src/
          - index.js
          - secret.js
        ```

        The following paths will be returned:

        ```yaml
        - assets/logos/logo.svg
        - src/index.js
        ```
        """
        return pulumi.get(self, "asset_paths")

    @property
    @pulumi.getter
    def assets(self) -> Optional[Mapping[str, Union[pulumi.Asset, pulumi.Archive]]]:
        """
        A map of assets found after running the command.
        The key is the relative path from the command dir
        """
        return pulumi.get(self, "assets")

    @property
    @pulumi.getter
    def command(self) -> str:
        """
        The command to run.
        """
        return pulumi.get(self, "command")

    @property
    @pulumi.getter
    def dir(self) -> Optional[str]:
        """
        The directory from which to run the command from. If `dir` does not exist, then
        `Command` will fail.
        """
        return pulumi.get(self, "dir")

    @property
    @pulumi.getter
    def environment(self) -> Optional[Mapping[str, str]]:
        """
        Additional environment variables available to the command's process.
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter
    def interpreter(self) -> Optional[Sequence[str]]:
        """
        The program and arguments to run the command.
        On Linux and macOS, defaults to: `["/bin/sh", "-c"]`. On Windows, defaults to: `["cmd", "/C"]`
        """
        return pulumi.get(self, "interpreter")

    @property
    @pulumi.getter
    def stderr(self) -> str:
        """
        The standard error of the command's process
        """
        return pulumi.get(self, "stderr")

    @property
    @pulumi.getter
    def stdin(self) -> Optional[str]:
        """
        Pass a string to the command's process as standard in
        """
        return pulumi.get(self, "stdin")

    @property
    @pulumi.getter
    def stdout(self) -> str:
        """
        The standard output of the command's process
        """
        return pulumi.get(self, "stdout")


class AwaitableRunResult(RunResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return RunResult(
            archive=self.archive,
            archive_paths=self.archive_paths,
            asset_paths=self.asset_paths,
            assets=self.assets,
            command=self.command,
            dir=self.dir,
            environment=self.environment,
            interpreter=self.interpreter,
            stderr=self.stderr,
            stdin=self.stdin,
            stdout=self.stdout)


def run(archive_paths: Optional[Sequence[str]] = None,
        asset_paths: Optional[Sequence[str]] = None,
        command: Optional[str] = None,
        dir: Optional[str] = None,
        environment: Optional[Mapping[str, str]] = None,
        interpreter: Optional[Sequence[str]] = None,
        stdin: Optional[str] = None,
        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableRunResult:
    """
    A local command to be executed.
    This command will always be run on any preview or deployment. Use `local.Command` to avoid duplicating executions.


    :param Sequence[str] archive_paths: A list of path globs to return as a single archive asset after the command completes.
           
           When specifying glob patterns the following rules apply:
           - We only include files not directories for assets and archives.
           - Path separators are `/` on all platforms - including Windows.
           - Patterns starting with `!` are 'exclude' rules.
           - Rules are evaluated in order, so exclude rules should be after inclusion rules.
           - `*` matches anything except `/`
           - `**` matches anything, _including_ `/`
           - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
           - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)
           
           #### Example
           
           Given the rules:
           ```yaml
           - "assets/**"
           - "src/**.js"
           - "!**secret.*"
           ```
           
           When evaluating against this folder:
           
           ```yaml
           - assets/
             - logos/
               - logo.svg
           - src/
             - index.js
             - secret.js
           ```
           
           The following paths will be returned:
           
           ```yaml
           - assets/logos/logo.svg
           - src/index.js
           ```
    :param Sequence[str] asset_paths: A list of path globs to read after the command completes.
           
           When specifying glob patterns the following rules apply:
           - We only include files not directories for assets and archives.
           - Path separators are `/` on all platforms - including Windows.
           - Patterns starting with `!` are 'exclude' rules.
           - Rules are evaluated in order, so exclude rules should be after inclusion rules.
           - `*` matches anything except `/`
           - `**` matches anything, _including_ `/`
           - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
           - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)
           
           #### Example
           
           Given the rules:
           ```yaml
           - "assets/**"
           - "src/**.js"
           - "!**secret.*"
           ```
           
           When evaluating against this folder:
           
           ```yaml
           - assets/
             - logos/
               - logo.svg
           - src/
             - index.js
             - secret.js
           ```
           
           The following paths will be returned:
           
           ```yaml
           - assets/logos/logo.svg
           - src/index.js
           ```
    :param str command: The command to run.
    :param str dir: The directory from which to run the command from. If `dir` does not exist, then
           `Command` will fail.
    :param Mapping[str, str] environment: Additional environment variables available to the command's process.
    :param Sequence[str] interpreter: The program and arguments to run the command.
           On Linux and macOS, defaults to: `["/bin/sh", "-c"]`. On Windows, defaults to: `["cmd", "/C"]`
    :param str stdin: Pass a string to the command's process as standard in
    """
    __args__ = dict()
    __args__['archivePaths'] = archive_paths
    __args__['assetPaths'] = asset_paths
    __args__['command'] = command
    __args__['dir'] = dir
    __args__['environment'] = environment
    __args__['interpreter'] = interpreter
    __args__['stdin'] = stdin
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('command:local:run', __args__, opts=opts, typ=RunResult).value

    return AwaitableRunResult(
        archive=pulumi.get(__ret__, 'archive'),
        archive_paths=pulumi.get(__ret__, 'archive_paths'),
        asset_paths=pulumi.get(__ret__, 'asset_paths'),
        assets=pulumi.get(__ret__, 'assets'),
        command=pulumi.get(__ret__, 'command'),
        dir=pulumi.get(__ret__, 'dir'),
        environment=pulumi.get(__ret__, 'environment'),
        interpreter=pulumi.get(__ret__, 'interpreter'),
        stderr=pulumi.get(__ret__, 'stderr'),
        stdin=pulumi.get(__ret__, 'stdin'),
        stdout=pulumi.get(__ret__, 'stdout'))


@_utilities.lift_output_func(run)
def run_output(archive_paths: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
               asset_paths: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
               command: Optional[pulumi.Input[str]] = None,
               dir: Optional[pulumi.Input[Optional[str]]] = None,
               environment: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
               interpreter: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
               stdin: Optional[pulumi.Input[Optional[str]]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[RunResult]:
    """
    A local command to be executed.
    This command will always be run on any preview or deployment. Use `local.Command` to avoid duplicating executions.


    :param Sequence[str] archive_paths: A list of path globs to return as a single archive asset after the command completes.
           
           When specifying glob patterns the following rules apply:
           - We only include files not directories for assets and archives.
           - Path separators are `/` on all platforms - including Windows.
           - Patterns starting with `!` are 'exclude' rules.
           - Rules are evaluated in order, so exclude rules should be after inclusion rules.
           - `*` matches anything except `/`
           - `**` matches anything, _including_ `/`
           - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
           - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)
           
           #### Example
           
           Given the rules:
           ```yaml
           - "assets/**"
           - "src/**.js"
           - "!**secret.*"
           ```
           
           When evaluating against this folder:
           
           ```yaml
           - assets/
             - logos/
               - logo.svg
           - src/
             - index.js
             - secret.js
           ```
           
           The following paths will be returned:
           
           ```yaml
           - assets/logos/logo.svg
           - src/index.js
           ```
    :param Sequence[str] asset_paths: A list of path globs to read after the command completes.
           
           When specifying glob patterns the following rules apply:
           - We only include files not directories for assets and archives.
           - Path separators are `/` on all platforms - including Windows.
           - Patterns starting with `!` are 'exclude' rules.
           - Rules are evaluated in order, so exclude rules should be after inclusion rules.
           - `*` matches anything except `/`
           - `**` matches anything, _including_ `/`
           - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
           - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)
           
           #### Example
           
           Given the rules:
           ```yaml
           - "assets/**"
           - "src/**.js"
           - "!**secret.*"
           ```
           
           When evaluating against this folder:
           
           ```yaml
           - assets/
             - logos/
               - logo.svg
           - src/
             - index.js
             - secret.js
           ```
           
           The following paths will be returned:
           
           ```yaml
           - assets/logos/logo.svg
           - src/index.js
           ```
    :param str command: The command to run.
    :param str dir: The directory from which to run the command from. If `dir` does not exist, then
           `Command` will fail.
    :param Mapping[str, str] environment: Additional environment variables available to the command's process.
    :param Sequence[str] interpreter: The program and arguments to run the command.
           On Linux and macOS, defaults to: `["/bin/sh", "-c"]`. On Windows, defaults to: `["cmd", "/C"]`
    :param str stdin: Pass a string to the command's process as standard in
    """
    ...
