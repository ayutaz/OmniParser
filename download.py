import os
from huggingface_hub import snapshot_download

# Set the repository name
repo_id = "microsoft/OmniParser"

# Set the local directory where you want to save the files
local_dir = "weights"

# Set cache directory (optional)
cache_dir = "/root/.cache/huggingface"

# Create the local directory if it doesn't exist
os.makedirs(local_dir, exist_ok=True)

# Download the entire repository
snapshot_download(repo_id, local_dir=local_dir, ignore_patterns=["*.md"], cache_dir=cache_dir)

print(f"All files and folders have been downloaded to {local_dir}")