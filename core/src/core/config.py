from pathlib import Path
from typing import Optional
from pydantic import BaseModel


class Config(BaseModel):
    PACKAGE_ROOT: Path
    GENERATIONS_DIR: Path
    MODELS_DIR: Path
    HF_TOKEN: Optional[str] = None
