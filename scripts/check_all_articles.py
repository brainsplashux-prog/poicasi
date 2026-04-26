# -*- coding: utf-8 -*-
"""全記事の公開状態と本文中のポイカジ言及を確認"""
import json
import urllib.request

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"

# 全記事を取得(limitを100に)
url = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles?limit=100&fields=id,title,slug,publishedAt,content"
req = urllib.request.Request(url, headers={"X-MICROCMS-API-KEY": API_KEY})
with urllib.request.urlopen(req) as res:
    data = json.loads(res.read())

with open("c:/tmp/all_articles_status.txt", "w", encoding="utf-8") as f:
    f.write(f"Total: {data['totalCount']} articles\n\n")
    for a in data["contents"]:
        slug = a.get("slug", "?")
        cid = a["id"]
        title = a.get("title", "?")[:60]
        status = "PUBLISHED" if a.get("publishedAt") else "DRAFT"
        content = a.get("content", "")
        has_poicasi = "ポイカジ" in content or "poicasi" in content.lower()
        flag = " ⚠️POICASI" if has_poicasi else ""
        f.write(f"[{status}] {slug}\n  ID: {cid}\n  Title: {title}\n  Poicasi mention: {has_poicasi}{flag}\n\n")

print("Done - c:/tmp/all_articles_status.txt")
