// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * A local command to be executed.
 * This command will always be run on any preview or deployment. Use `local.Command` to avoid duplicating executions.
 */
export function run(args: RunArgs, opts?: pulumi.InvokeOptions): Promise<RunResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("command:local:run", {
        "addPreviousOutputInEnv": args.addPreviousOutputInEnv,
        "archivePaths": args.archivePaths,
        "assetPaths": args.assetPaths,
        "command": args.command,
        "dir": args.dir,
        "environment": args.environment,
        "interpreter": args.interpreter,
        "logging": args.logging,
        "stdin": args.stdin,
    }, opts);
}

export interface RunArgs {
    /**
     * If the previous command's stdout and stderr (as generated by the prior create/update) is
     * injected into the environment of the next run as PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR.
     * Defaults to true.
     */
    addPreviousOutputInEnv?: boolean;
    /**
     * A list of path globs to return as a single archive asset after the command completes.
     *
     * When specifying glob patterns the following rules apply:
     * - We only include files not directories for assets and archives.
     * - Path separators are `/` on all platforms - including Windows.
     * - Patterns starting with `!` are 'exclude' rules.
     * - Rules are evaluated in order, so exclude rules should be after inclusion rules.
     * - `*` matches anything except `/`
     * - `**` matches anything, _including_ `/`
     * - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
     * - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)
     *
     * #### Example
     *
     * Given the rules:
     * ```yaml
     * - "assets/**"
     * - "src/**.js"
     * - "!**secret.*"
     * ```
     *
     * When evaluating against this folder:
     *
     * ```yaml
     * - assets/
     *   - logos/
     *     - logo.svg
     * - src/
     *   - index.js
     *   - secret.js
     * ```
     *
     * The following paths will be returned:
     *
     * ```yaml
     * - assets/logos/logo.svg
     * - src/index.js
     * ```
     */
    archivePaths?: string[];
    /**
     * A list of path globs to read after the command completes.
     *
     * When specifying glob patterns the following rules apply:
     * - We only include files not directories for assets and archives.
     * - Path separators are `/` on all platforms - including Windows.
     * - Patterns starting with `!` are 'exclude' rules.
     * - Rules are evaluated in order, so exclude rules should be after inclusion rules.
     * - `*` matches anything except `/`
     * - `**` matches anything, _including_ `/`
     * - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
     * - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)
     *
     * #### Example
     *
     * Given the rules:
     * ```yaml
     * - "assets/**"
     * - "src/**.js"
     * - "!**secret.*"
     * ```
     *
     * When evaluating against this folder:
     *
     * ```yaml
     * - assets/
     *   - logos/
     *     - logo.svg
     * - src/
     *   - index.js
     *   - secret.js
     * ```
     *
     * The following paths will be returned:
     *
     * ```yaml
     * - assets/logos/logo.svg
     * - src/index.js
     * ```
     */
    assetPaths?: string[];
    /**
     * The command to run.
     */
    command: string;
    /**
     * The directory from which to run the command from. If `dir` does not exist, then
     * `Command` will fail.
     */
    dir?: string;
    /**
     * Additional environment variables available to the command's process.
     */
    environment?: {[key: string]: string};
    /**
     * The program and arguments to run the command.
     * On Linux and macOS, defaults to: `["/bin/sh", "-c"]`. On Windows, defaults to: `["cmd", "/C"]`
     */
    interpreter?: string[];
    /**
     * If the command's stdout and stderr should be logged. This doesn't affect the capturing of
     * stdout and stderr as outputs. If there might be secrets in the output, you can disable logging here and mark the
     * outputs as secret via 'additionalSecretOutputs'. Defaults to logging both stdout and stderr.
     */
    logging?: enums.common.Logging;
    /**
     * Pass a string to the command's process as standard in
     */
    stdin?: string;
}

export interface RunResult {
    /**
     * If the previous command's stdout and stderr (as generated by the prior create/update) is
     * injected into the environment of the next run as PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR.
     * Defaults to true.
     */
    readonly addPreviousOutputInEnv?: boolean;
    /**
     * An archive asset containing files found after running the command.
     */
    readonly archive?: pulumi.asset.Archive;
    /**
     * A list of path globs to return as a single archive asset after the command completes.
     *
     * When specifying glob patterns the following rules apply:
     * - We only include files not directories for assets and archives.
     * - Path separators are `/` on all platforms - including Windows.
     * - Patterns starting with `!` are 'exclude' rules.
     * - Rules are evaluated in order, so exclude rules should be after inclusion rules.
     * - `*` matches anything except `/`
     * - `**` matches anything, _including_ `/`
     * - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
     * - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)
     *
     * #### Example
     *
     * Given the rules:
     * ```yaml
     * - "assets/**"
     * - "src/**.js"
     * - "!**secret.*"
     * ```
     *
     * When evaluating against this folder:
     *
     * ```yaml
     * - assets/
     *   - logos/
     *     - logo.svg
     * - src/
     *   - index.js
     *   - secret.js
     * ```
     *
     * The following paths will be returned:
     *
     * ```yaml
     * - assets/logos/logo.svg
     * - src/index.js
     * ```
     */
    readonly archivePaths?: string[];
    /**
     * A list of path globs to read after the command completes.
     *
     * When specifying glob patterns the following rules apply:
     * - We only include files not directories for assets and archives.
     * - Path separators are `/` on all platforms - including Windows.
     * - Patterns starting with `!` are 'exclude' rules.
     * - Rules are evaluated in order, so exclude rules should be after inclusion rules.
     * - `*` matches anything except `/`
     * - `**` matches anything, _including_ `/`
     * - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
     * - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)
     *
     * #### Example
     *
     * Given the rules:
     * ```yaml
     * - "assets/**"
     * - "src/**.js"
     * - "!**secret.*"
     * ```
     *
     * When evaluating against this folder:
     *
     * ```yaml
     * - assets/
     *   - logos/
     *     - logo.svg
     * - src/
     *   - index.js
     *   - secret.js
     * ```
     *
     * The following paths will be returned:
     *
     * ```yaml
     * - assets/logos/logo.svg
     * - src/index.js
     * ```
     */
    readonly assetPaths?: string[];
    /**
     * A map of assets found after running the command.
     * The key is the relative path from the command dir
     */
    readonly assets?: {[key: string]: pulumi.asset.Asset | pulumi.asset.Archive};
    /**
     * The command to run.
     */
    readonly command: string;
    /**
     * The directory from which to run the command from. If `dir` does not exist, then
     * `Command` will fail.
     */
    readonly dir?: string;
    /**
     * Additional environment variables available to the command's process.
     */
    readonly environment?: {[key: string]: string};
    /**
     * The program and arguments to run the command.
     * On Linux and macOS, defaults to: `["/bin/sh", "-c"]`. On Windows, defaults to: `["cmd", "/C"]`
     */
    readonly interpreter?: string[];
    /**
     * If the command's stdout and stderr should be logged. This doesn't affect the capturing of
     * stdout and stderr as outputs. If there might be secrets in the output, you can disable logging here and mark the
     * outputs as secret via 'additionalSecretOutputs'. Defaults to logging both stdout and stderr.
     */
    readonly logging?: enums.common.Logging;
    /**
     * The standard error of the command's process
     */
    readonly stderr: string;
    /**
     * Pass a string to the command's process as standard in
     */
    readonly stdin?: string;
    /**
     * The standard output of the command's process
     */
    readonly stdout: string;
}
/**
 * A local command to be executed.
 * This command will always be run on any preview or deployment. Use `local.Command` to avoid duplicating executions.
 */
export function runOutput(args: RunOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<RunResult> {
    return pulumi.output(args).apply((a: any) => run(a, opts))
}

export interface RunOutputArgs {
    /**
     * If the previous command's stdout and stderr (as generated by the prior create/update) is
     * injected into the environment of the next run as PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR.
     * Defaults to true.
     */
    addPreviousOutputInEnv?: pulumi.Input<boolean>;
    /**
     * A list of path globs to return as a single archive asset after the command completes.
     *
     * When specifying glob patterns the following rules apply:
     * - We only include files not directories for assets and archives.
     * - Path separators are `/` on all platforms - including Windows.
     * - Patterns starting with `!` are 'exclude' rules.
     * - Rules are evaluated in order, so exclude rules should be after inclusion rules.
     * - `*` matches anything except `/`
     * - `**` matches anything, _including_ `/`
     * - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
     * - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)
     *
     * #### Example
     *
     * Given the rules:
     * ```yaml
     * - "assets/**"
     * - "src/**.js"
     * - "!**secret.*"
     * ```
     *
     * When evaluating against this folder:
     *
     * ```yaml
     * - assets/
     *   - logos/
     *     - logo.svg
     * - src/
     *   - index.js
     *   - secret.js
     * ```
     *
     * The following paths will be returned:
     *
     * ```yaml
     * - assets/logos/logo.svg
     * - src/index.js
     * ```
     */
    archivePaths?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of path globs to read after the command completes.
     *
     * When specifying glob patterns the following rules apply:
     * - We only include files not directories for assets and archives.
     * - Path separators are `/` on all platforms - including Windows.
     * - Patterns starting with `!` are 'exclude' rules.
     * - Rules are evaluated in order, so exclude rules should be after inclusion rules.
     * - `*` matches anything except `/`
     * - `**` matches anything, _including_ `/`
     * - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
     * - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)
     *
     * #### Example
     *
     * Given the rules:
     * ```yaml
     * - "assets/**"
     * - "src/**.js"
     * - "!**secret.*"
     * ```
     *
     * When evaluating against this folder:
     *
     * ```yaml
     * - assets/
     *   - logos/
     *     - logo.svg
     * - src/
     *   - index.js
     *   - secret.js
     * ```
     *
     * The following paths will be returned:
     *
     * ```yaml
     * - assets/logos/logo.svg
     * - src/index.js
     * ```
     */
    assetPaths?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The command to run.
     */
    command: pulumi.Input<string>;
    /**
     * The directory from which to run the command from. If `dir` does not exist, then
     * `Command` will fail.
     */
    dir?: pulumi.Input<string>;
    /**
     * Additional environment variables available to the command's process.
     */
    environment?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The program and arguments to run the command.
     * On Linux and macOS, defaults to: `["/bin/sh", "-c"]`. On Windows, defaults to: `["cmd", "/C"]`
     */
    interpreter?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * If the command's stdout and stderr should be logged. This doesn't affect the capturing of
     * stdout and stderr as outputs. If there might be secrets in the output, you can disable logging here and mark the
     * outputs as secret via 'additionalSecretOutputs'. Defaults to logging both stdout and stderr.
     */
    logging?: pulumi.Input<enums.common.Logging>;
    /**
     * Pass a string to the command's process as standard in
     */
    stdin?: pulumi.Input<string>;
}
