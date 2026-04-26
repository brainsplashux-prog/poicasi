# -*- coding: utf-8 -*-
"""microCMS共通クライアント"""
import json
import urllib.request
import time

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

def post_draft(data):
    """記事を下書きとしてPOST"""
    body = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=body,
        headers={
            "X-MICROCMS-API-KEY": API_KEY,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as res:
            result = json.loads(res.read())
            return ("OK", data.get("title", "?")[:40], result.get("id", "?"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        return ("FAIL", data.get("title", "?")[:40], f"{e.code}: {error_body[:200]}")

def post_all(articles, output_file="c:/tmp/post_results.txt"):
    """記事リストを投稿して結果をファイルに書き出す"""
    results = []
    for i, art in enumerate(articles, 1):
        slug = art.get("slug", "?")
        print(f"[{i}/{len(articles)}] {slug}")
        result = post_draft(art)
        results.append(f"{result[0]}: {slug} ({result[1]}) -> {result[2]}")
        time.sleep(0.5)  # rate limit
    
    with open(output_file, "w", encoding="utf-8") as f:
        for r in results:
            f.write(r + "\n")
    print(f"Done - results in {output_file}")
    return results
