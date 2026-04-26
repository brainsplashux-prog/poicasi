# -*- coding: utf-8 -*-
"""体験データを含むW1記事を下書き（非公開）に戻す

microCMS PATCH API に ?status=draft クエリパラメータを付けて
非空のボディを送信することで、公開中の記事を下書き状態に変更する。
"""
import json
import urllib.request

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"

# 体験データを含む記事
ARTICLES_TO_UNPUBLISH = [
    ("6y_9l3-nb186", "game-poikatsu-guide-2026", "P01"),
    ("8321cbrkqa", "poicasi-vs-poinyam-vs-boxmerge", "C01"),
    ("658aonzbm7u", "poicasi-howto-guide", "H01"),
]

results = []

for content_id, slug, article_id in ARTICLES_TO_UNPUBLISH:
    # ?status=draft で下書きに戻す。ボディには何か1フィールド送る必要がある
    url = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles/{content_id}?status=draft"
    # descriptionフィールドを同じ値で送る（実質変更なし）
    body = json.dumps({"description": ""}).encode("utf-8")
    req = urllib.request.Request(
        url, data=body,
        headers={"X-MICROCMS-API-KEY": API_KEY, "Content-Type": "application/json"},
        method="PATCH",
    )
    try:
        with urllib.request.urlopen(req) as res:
            results.append(f"OK: {article_id} ({slug}) -> DRAFT")
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        results.append(f"FAIL ({e.code}): {article_id} ({slug}) - {error_body[:300]}")

with open("c:/tmp/unpublish_results3.txt", "w", encoding="utf-8") as f:
    for r in results:
        f.write(r + "\n")

print("Done - results in c:/tmp/unpublish_results3.txt")
