import requests
import os

EXT_FILE = "extensions.txt"
OUTPUT_DIR = "vsix_downloads"
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(EXT_FILE, "r", encoding="utf-8") as f:
    extensions = [line.strip() for line in f if line.strip()]

for ext_id in extensions:
    try:
        publisher, name = ext_id.split(".")
        url = f"https://marketplace.visualstudio.com/_apis/public/gallery/publishers/{publisher}/vsextensions/{name}/latest/vspackage"
        print(f"Downloading {ext_id}...")
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        with open(os.path.join(OUTPUT_DIR, f"{ext_id}.vsix"), "wb") as out:
            out.write(resp.content)
        print(f"Success: {ext_id}.vsix")
    except Exception as e:
        print(f"Failed: {ext_id} - {e}")
