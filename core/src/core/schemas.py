from pathlib import Path
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
# from datetime import datetime, timezone, timedelta


class GenerationRecord(BaseModel):
    """
    Represents a TTS generation record.

    Attributes:
        id (UUID): Unique identifier for the generation.
        text (str): The input text for TTS.
        model_name (str): The name of the TTS model used.
        piper_config (Optional[str]): Optional Piper configuration used.
        audio_path (Path): Path to the generated audio file.
    """

    id: UUID = Field(default_factory=lambda: uuid4())
    text: str
    model_name: str
    piper_config: str = Field(
        default_factory=lambda val: val.to_dict() if val else None
    )
    audio_path: str


class PiperModel(BaseModel):
    """
    Represents a Piper TTS model.
    Attributes:
        name (str): The name of the model.
        onnx_path (Path): Path to the ONNX model file.
        config_path (Optional[Path]): Optional path to the model configuration file.
    """
    name: str
    onnx_path: Path
    config_path: Path | None = None


class TTSRequest(BaseModel):
    """
    Represents a text-to-speech (TTS) request.
    Attributes:
        text (str): The input text for TTS.
        voice (str | None): The voice to use for TTS.
        speaker_id (int | None): The ID of the speaker to use for TTS.
    """
    text: str
    voice: str | None = None
    speaker_id: int | None = None
