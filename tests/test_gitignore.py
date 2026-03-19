from __future__ import annotations

import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_python_bytecode_artifacts_are_ignored() -> None:
    ignored_paths = [
        "ethan/__pycache__/quick_sort.cpython-313.pyc",
        "tests/__pycache__/test_quick_sort.cpython-313.pyc",
    ]
    result = subprocess.run(
        ["git", "check-ignore", *ignored_paths],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert result.stdout.splitlines() == ignored_paths
