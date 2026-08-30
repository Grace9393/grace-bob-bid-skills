from __future__ import annotations

import platform
from pathlib import Path


def runtime_python_packages() -> tuple[str, ...]:
    return (
        "bm25s",
    )


def skill_dir() -> Path:
    return Path(__file__).resolve().parent.parent


def venv_python() -> Path:
    root = skill_dir() / ".venv"
    if platform.system() == "Windows":
        return root / "Scripts" / "python.exe"
    return root / "bin" / "python"


def venv_executable(name: str) -> Path:
    root = skill_dir() / ".venv"
    if platform.system() == "Windows":
        return root / "Scripts" / f"{name}.exe"
    return root / "bin" / name


def zvec_store_path() -> Path:
    return skill_dir() / "references" / "bid_library_zvec"
