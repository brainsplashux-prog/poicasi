# -*- coding: utf-8 -*-
"""全ゲーム攻略記事のcategoryとarticleTypeを一括設定"""
import json, sys, urllib.request
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
BASE = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

def get_all():
    req = urllib.request.Request(f"{BASE}?limit=100",
        headers={"X-MICROCMS-API-KEY": API_KEY})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())["contents"]

def patch(article_id, data):
    body = json.dumps(data, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(f"{BASE}/{article_id}", data=body,
        headers={"X-MICROCMS-API-KEY": API_KEY, "Content-Type": "application/json"},
        method="PATCH")
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

if __name__ == "__main__":
    articles = get_all()
    # ゲーム攻略記事のslugパターン
    game_slugs = [
        "rise-of-kingdoms-poikatsu-guide",
        "dragon-city-poikatsu-guide",
        "monster-basket-poikatsu-guide",
        "coin-master-poikatsu-guide",
        "clash-of-clans-poikatsu-guide",
        "lords-mobile-poikatsu-guide",
        "gardenscapes-poikatsu-guide",
        "viking-rise-poikatsu-guide",
        "mafia-city-poikatsu-guide",
        "state-of-survival-poikatsu-guide",
        "vivid-army-poikatsu-guide",
        "brawl-stars-poikatsu-guide",
        "homescapes-poikatsu-guide",
        "final-gear-poikatsu-guide",
        "evertale-poikatsu-guide",
    ]
    ok = 0
    for a in articles:
        if a.get("slug") in game_slugs:
            patch(a["id"], {"category": ["ゲーム攻略"], "articleType": ["game-guide"]})
            print(f"[OK] {a['slug'][:50]}")
            ok += 1
    print(f"\n完了: {ok}件 更新")
