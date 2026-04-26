# -*- coding: utf-8 -*-
"""microCMS管理APIのアップロードテスト（1ファイルのみ）"""
import json
import urllib.request
import os
import glob

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
MEDIA_ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms-management.io/api/v1/media"

# テスト画像
IMAGE_DIR = r"C:\Users\dyesi\.gemini\antigravity\brain\8fd02cc1-ead1-4569-854a-da33fd25b97f"
files = glob.glob(os.path.join(IMAGE_DIR, "eyecatch_ranking_*.png"))
if not files:
    print("No test image found")
    exit(1)

filepath = files[0]
filename = os.path.basename(filepath)
filesize = os.path.getsize(filepath)
print(f"File: {filename}")
print(f"Size: {filesize} bytes ({filesize/1024/1024:.1f} MB)")

with open(filepath, "rb") as f:
    image_data = f.read()

print(f"Read {len(image_data)} bytes")

# Try multipart upload
boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
body = (
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
    f"Content-Type: image/png\r\n\r\n"
).encode("utf-8") + image_data + f"\r\n--{boundary}--\r\n".encode("utf-8")

print(f"Body size: {len(body)} bytes")
print(f"Endpoint: {MEDIA_ENDPOINT}")

req = urllib.request.Request(
    MEDIA_ENDPOINT,
    data=body,
    headers={
        "X-MICROCMS-API-KEY": API_KEY,
        "Content-Type": f"multipart/form-data; boundary={boundary}",
    },
    method="POST",
)

try:
    with urllib.request.urlopen(req) as res:
        result = json.loads(res.read())
        print(f"Success! URL: {result.get('url')}")
        print(f"Full response: {json.dumps(result, indent=2)}")
except urllib.error.HTTPError as e:
    error_body = e.read().decode("utf-8")
    print(f"HTTP Error: {e.code}")
    print(f"Headers: {dict(e.headers)}")
    print(f"Body: {error_body[:500]}")
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
