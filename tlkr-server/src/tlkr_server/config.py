"""
Configuration constants for tlkr-server.
"""

import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

APP_ROOT = Path(__file__).parent.parent.parent.resolve()
GENERATIONS_DIR = APP_ROOT / "generations"
MODELS_DIR = APP_ROOT / "models"
# Nothing needs to use HF_TOKEN directly as long as its loaded from the env if
# present. Downloading models from HF might block the request, so having this
# to check beforehand is useful for custom checking logic if I chose to add it
# later.
HF_TOKEN: Optional[str] = os.getenv("HF_TOKEN")
