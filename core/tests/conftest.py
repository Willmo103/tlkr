"""Test configuration that ensures `core/src` is importable.

This allows `import core` from tests when running in the core package root.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
