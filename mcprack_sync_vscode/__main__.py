from __future__ import annotations

import sys

from mcprack_client.cli import run_cli

from .paths import vscode_config_path


def main(argv: list[str] | None = None) -> int:
    return run_cli(
        prog="mcprack-sync-vscode",
        description="Keep VS Code Copilot MCP config in sync with mcprack",
        tool="vscode",
        api_client="vscode",
        servers_key="servers",
        resolve_config_path=vscode_config_path,
        argv=argv,
    )


if __name__ == "__main__":
    raise SystemExit(main())
