"""Resolve VS Code Copilot MCP config paths."""

from __future__ import annotations

import os
import sys
from pathlib import Path


def _home() -> Path:
    return Path.home()


def _candidates() -> list[Path]:
    home = _home()
    if sys.platform == "darwin":
        base = home / "Library" / "Application Support"
        return [
            base / "Code" / "User" / "mcp.json",
            base / "Code - Insiders" / "User" / "mcp.json",
        ]
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA", str(home / "AppData" / "Roaming"))
        return [
            Path(appdata) / "Code" / "User" / "mcp.json",
            Path(appdata) / "Code - Insiders" / "User" / "mcp.json",
        ]
    xdg = Path(os.environ.get("XDG_CONFIG_HOME", str(home / ".config")))
    return [
        xdg / "Code" / "User" / "mcp.json",
        xdg / "Code - Insiders" / "User" / "mcp.json",
    ]


def vscode_config_path() -> Path:
    """Prefer an existing mcp.json; otherwise the stable VS Code User path."""
    candidates = _candidates()
    for path in candidates:
        if path.is_file():
            return path
    return candidates[0]
