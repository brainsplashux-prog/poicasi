# -*- coding: utf-8 -*-
"""eyecatchフィールドの型確認テスト"""
import json
import urllib.request

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ARTICLES_ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

test_article_id = "vwue-yktf5b"
test_image_url = "https://hp.poicasi.co.jp/eyecatch/eyecatch_ranking_1775093010942.png"

# Test 1: URL string
print("=== Test 1: URL string ===")
patch_data = json.dumps({"eyecatch": test_image_url}).encode("utf-8")
req = urllib.request.Request(
    f"{ARTICLES_ENDPOINT}/{test_article_id}",
    data=patch_data,
    headers={"X-MICROCMS-API-KEY": API_KEY, "Content-Type": "application/json"},
    method="PATCH",
)
try:
    with urllib.request.urlopen(req) as res:
        print(f"OK: {json.loads(res.read())}")
except urllib.error.HTTPError as e:
    print(f"Error {e.code}: {e.read().decode('utf-8')}")

# Test 2: object with url key
print("\n=== Test 2: {url: ...} ===")
patch_data = json.dumps({"eyecatch": {"url": test_image_url}}).encode("utf-8")
req = urllib.request.Request(
    f"{ARTICLES_ENDPOINT}/{test_article_id}",
    data=patch_data,
    headers={"X-MICROCMS-API-KEY": API_KEY, "Content-Type": "application/json"},
    method="PATCH",
)
try:
    with urllib.request.urlopen(req) as res:
        print(f"OK: {json.loads(res.read())}")
except urllib.error.HTTPError as e:
    print(f"Error {e.code}: {e.read().decode('utf-8')}")

# Test 3: object with url and height/width
print("\n=== Test 3: {url: ..., height: ..., width: ...} ===")
patch_data = json.dumps({"eyecatch": {"url": test_image_url, "height": 1024, "width": 1024}}).encode("utf-8")
req = urllib.request.Request(
    f"{ARTICLES_ENDPOINT}/{test_article_id}",
    data=patch_data,
    headers={"X-MICROCMS-API-KEY": API_KEY, "Content-Type": "application/json"},
    method="PATCH",
)
try:
    with urllib.request.urlopen(req) as res:
        print(f"OK: {json.loads(res.read())}")
except urllib.error.HTTPError as e:
    print(f"Error {e.code}: {e.read().decode('utf-8')}")

# Test 4: look at API schema
print("\n=== Checking API schema ===")
req = urllib.request.Request(
    f"{ARTICLES_ENDPOINT}/{test_article_id}",
    headers={"X-MICROCMS-API-KEY": API_KEY},
)
with urllib.request.urlopen(req) as res:
    data = json.loads(res.read())
    # Show all keys and their types
    for key, value in data.items():
        if key != "content":
            print(f"  {key}: {type(value).__name__} = {str(value)[:100]}")
