from huggingface_hub import snapshot_download
from pathlib import Path
from config import MODELS_DIR

# The repository we want to download from
repo_id = "rhasspy/piper-voices"

# The specific folder we want (e.g., "en_US")
folder_to_download = "en/en_US"

local_dir = Path("./downloaded_voices")

print(f"Downloading folder '{folder_to_download}' from '{repo_id}'...")

# Use snapshot_download to get only the desired folder
snapshot_download(
    repo_id=repo_id,
    allow_patterns=[
        f"{folder_to_download}/*onnx*",
        "{folder_to_download}/*MODEL_CARD",
    ],  # This pattern matches all .onnx files inside the folder
    local_dir=local_dir,
    local_dir_use_symlinks=False,  # Use False on Windows for direct copies
    repo_type="model",
)

print("indexing downloaded models...")

for model_file in local_dir.rglob("*.onnx"):
