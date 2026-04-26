# -*- coding: utf-8 -*-
"""ポイカジ言及記事を非公開(下書き)に戻す - PATCH で status を DRAFT に"""
import json
import urllib.request
import time

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

# ポイカジを比較・推薦している記事のID一覧
UNPUBLISH_IDS = [
    ("4k6nbgnma", "cute-character-poikatsu-5apps"),
    ("7ma92nf07f", "eye-friendly-poikatsu-app"),
    ("g4v2nr8qcgz", "retro-medal-game-smartphone-report"),
    ("tsgkymug4se", "poikatsu-gambling-like-legal"),
    ("x5xktmk2e", "poikatsu-double-point-technique"),
    ("864g17pmc", "vpoint-paypay-exchange-guide"),
    ("qgsyd3cx2", "poikatsu-osusume-2026"),
    ("xh6ec8y9o124", "new-poikatsu-apps-2026"),
    ("3snifmz8w", "safe-poikatsu-guide"),
    ("21l-rly7u9o", "30sec-poikatsu-1month-verify"),
    ("bcymqgr_v_l", "poikatsu-stress-relief-games"),
    ("5l02ldebh", "casual-game-point-app-comparison"),
    ("0zd4sxi_f", "poinyam-2weeks-honest-review"),
    ("f2x4rg6spwl", "next-poikatsu-after-walking-apps"),
    ("6v9lshi1x", "poikatsu-trend-monthly-202604"),
    ("dhxh-s5zxfa", "no-boredom-poikatsu-guide"),
    ("i-f1x1v9d7", "medal-game-app-free-5"),
    ("azlq16uxp0g", "poicasi-30days-review"),
    ("dbjmexclpy", "point-site-rate-comparison-2026"),
    ("z25dbis3k", "poikatsu-app-ranking-top15"),
    ("vqnwvz_d2", "sukima-jikan-poikatsu-tips"),
    ("a2fpyh87x", "low-ads-poikatsu-app-ranking"),
    ("qr65q3r9v3gm", "vpoint-paypay-exchange-start"),
    ("658aonzbm7u", "poicasi-howto-guide"),
    ("8321cbrkqa", "poicasi-vs-poinyam-vs-boxmerge"),
    ("6y_9l3-nb186", "game-poikatsu-guide-2026"),
]

results = []
for cid, slug in UNPUBLISH_IDS:
    url = f"{ENDPOINT}/{cid}"
    # microCMS: PATCH with status array to change publish state
    body = json.dumps({"status": ["DRAFT"]}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "X-MICROCMS-API-KEY": API_KEY,
            "Content-Type": "application/json",
        },
        method="PATCH",
    )
    try:
        with urllib.request.urlopen(req) as res:
            results.append(f"OK: {slug} -> DRAFT")
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8")[:300]
        results.append(f"FAIL({e.code}): {slug} -> {err}")
    time.sleep(0.3)

with open("c:/tmp/unpublish_v2_results.txt", "w", encoding="utf-8") as f:
    for r in results:
        f.write(r + "\n")
    f.write(f"\nTotal: {len(results)} articles processed\n")

print(f"Done - {len(results)} articles processed")
for r in results[:5]:
    print(r[:80])
