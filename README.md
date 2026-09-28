# mcprack-sync-vscode

Keep **VS Code** (GitHub Copilot MCP) server configuration up to date from a
[mcprack](https://github.com/VitexSoftware/mcprack) catalog.

## Install

```bash
sudo apt install mcprack-sync-vscode
```

## Setup

```bash
mcprack-sync-vscode configure \
  --url https://mcprack.example.com \
  --token mcr_your_token_here

mcprack-sync-vscode sync
mcprack-sync-vscode sync --dry-run
mcprack-sync-vscode status
```

Default target (Linux): `~/.config/Code/User/mcp.json` (uses Code Insiders
path if that file already exists and the stable one does not).

Merges the `servers` key (VS Code / Copilot shape). Local-only servers are
preserved unless you pass `--replace`.

## Timer

```bash
systemctl --user enable --now mcprack-sync-vscode.timer
```

## License

MIT
