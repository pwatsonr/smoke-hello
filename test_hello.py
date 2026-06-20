import subprocess
import sys
from pathlib import Path

from hello import greet

SCRIPT = Path(__file__).parent / "hello.py"


def test_hello_prints_hello_world() -> None:
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True,
        text=True,
        timeout=5,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "hello world"
    assert result.stderr == ""


def test_greet_default_returns_hello_world() -> None:
    assert greet() == "hello world"


def test_greet_with_custom_name_returns_hello_name() -> None:
    assert greet("ada") == "hello ada"
