from pathlib import Path
from uuid import UUID
import pytest

from core.schemas import GenerationRecord, PiperModel, TTSRequest  # noqa
from core.config import Config  # noqa


def test_generation_record_defaults_and_types(tmp_path: Path):
    audio_file = tmp_path / "sample.wav"
    # Simulate path as string per schema definition
    record = GenerationRecord(
        text="Hello world",
        model_name="piper-en-us",
        audio_path=str(audio_file),
    )

    assert isinstance(record.id, UUID)
    assert record.text == "Hello world"
    assert record.model_name == "piper-en-us"
    assert record.piper_config is None
    assert record.audio_path == str(audio_file)


def test_generation_record_all_fields(tmp_path: Path):
    audio_file = tmp_path / "a.wav"
    record = GenerationRecord(
        text="Hi",
        model_name="model-x",
        piper_config="{\"noise_scale\":0.5}",
        audio_path=str(audio_file),
    )

    assert record.piper_config == "{\"noise_scale\":0.5}"


def test_piper_model_paths(tmp_path: Path):
    onnx = tmp_path / "model.onnx"
    cfg = tmp_path / "config.json"
    model = PiperModel(name="m", onnx_path=onnx, config_path=cfg)

    assert model.name == "m"
    assert model.onnx_path == onnx
    assert model.config_path == cfg


def test_piper_model_optional_config(tmp_path: Path):
    onnx = tmp_path / "model.onnx"
    model = PiperModel(name="m", onnx_path=onnx)
    assert model.config_path is None


@pytest.mark.parametrize(
    "text,voice,speaker_id",
    [
        ("Hello", None, None),
        ("Hi", "alloy", 1),
        ("Hola", "bella", None),
    ],
)
def test_tts_request_variants(text, voice, speaker_id):
    req = TTSRequest(text=text, voice=voice, speaker_id=speaker_id)
    assert req.text == text
    assert req.voice == voice
    assert req.speaker_id == speaker_id


def test_config_model(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    pkg = tmp_path / "pkg"
    gens = tmp_path / "gens"
    models = tmp_path / "models"

    cfg = Config(
        PACKAGE_ROOT=pkg,
        GENERATIONS_DIR=gens,
        MODELS_DIR=models,
        HF_TOKEN=None,
    )

    assert cfg.PACKAGE_ROOT == pkg
    assert cfg.GENERATIONS_DIR == gens
    assert cfg.MODELS_DIR == models
    assert cfg.HF_TOKEN is None
