# -*- coding: utf-8 -*-
"""差し替え結果を検証"""
import json
import urllib.request
import re

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"

# 全記事取得
url = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles?limit=50&fields=id,title,slug,content&orders=-publishedAt"
req = urllib.request.Request(url, headers={"X-MICROCMS-API-KEY": API_KEY})
with urllib.request.urlopen(req) as res:
    data = json.loads(res.read())

print(f"Total articles: {data['totalCount']}\n")

old_count = 0
new_count = 0
no_img = 0

for a in data["contents"]:
    aid = a["id"]
    title = a["title"][:50]
    content = a.get("content", "")
    
    m = re.search(r'src="([^"]*eyecatch[^"]*)"', content)
    if m:
        url = m.group(1)
        is_new = "1775093" in url
        if is_new:
            new_count += 1
            status = "✅ NEW"
        else:
            old_count += 1
            status = "❌ OLD"
        print(f"{status} | {aid} | {title}")
        print(f"       URL: {url}")
    else:
        no_img += 1
        print(f"⚠️ NO IMG | {aid} | {title}")
    print()

# URLアクセスチェック（1つだけ）
print("=== URL Access Check ===")
test_url = "https://media.poicasi.co.jp/eyecatch/eyecatch_ranking_1775093010942.png"
try:
    req = urllib.request.Request(test_url, method="HEAD")
    with urllib.request.urlopen(req) as res:
        print(f"✅ {test_url} -> {res.status}")
except Exception as e:
    print(f"❌ {test_url} -> {e}")

print(f"\n=== Summary ===")
print(f"New images: {new_count}")
print(f"Old images: {old_count}")
print(f"No images: {no_img}")
