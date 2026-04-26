# -*- coding: utf-8 -*-
"""Batch3-4の8記事を公開状態にする (修正版)"""
import json
import urllib.request
import time

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"

# 公開対象のslug一覧
TARGET_SLUGS = [
    "poikatsu-game-dl-vs-jousetsu",
    "poikatsu-game-demerit-5",
    "poikatsu-game-waste-of-time",
    "poikatsu-game-dl-checklist",
    "poikatsu-game-kakin-hitsuyou",
    "poikatsu-game-storage-light",
    "poikatsu-game-same-app-earn",
    "poikatsu-game-dl-vs-jousetsu-chart",
]

# 全記事を取得してslugからIDを特定
url = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles?limit=100&fields=id,slug,title"
req = urllib.request.Request(url, headers={"X-MICROCMS-API-KEY": API_KEY})
with urllib.request.urlopen(req) as res:
    data = json.loads(res.read())

slug_to_id = {}
for a in data["contents"]:
    s = a.get("slug", "")
    if s in TARGET_SLUGS:
        slug_to_id[s] = (a["id"], a.get("title", "?")[:50])

print(f"Found {len(slug_to_id)}/{len(TARGET_SLUGS)} articles to publish\n")

results = []
for slug in TARGET_SLUGS:
    if slug not in slug_to_id:
        print(f"  SKIP: {slug} (not found)")
        results.append(f"SKIP: {slug} (not found)")
        continue
    
    cid, title = slug_to_id[slug]
    # PATCHにはダミーのフィールド更新を含める（空bodyは拒否されるため）
    patch_url = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles/{cid}?status=PUBLISH"
    # titleをそのまま再設定することでbody非空にする
    body = json.dumps({"title": title}).encode("utf-8")
    req = urllib.request.Request(
        patch_url,
        data=body,
        headers={
            "X-MICROCMS-API-KEY": API_KEY,
            "Content-Type": "application/json",
        },
        method="PATCH",
    )
    try:
        with urllib.request.urlopen(req) as res:
            print(f"  OK: {slug} -> PUBLISHED")
            results.append(f"OK: {slug} ({title})")
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8")[:200]
        print(f"  FAIL: {slug} -> {e.code}: {err}")
        results.append(f"FAIL: {slug} ({e.code}: {err})")
    time.sleep(0.5)

with open("c:/tmp/publish_batch3_4_v2_results.txt", "w", encoding="utf-8") as f:
    for r in results:
        f.write(r + "\n")
print(f"\nDone - results in c:/tmp/publish_batch3_4_v2_results.txt")
