# -*- coding: utf-8 -*-
"""全記事のCTAボックスリンクを https://poicasi.co.jp から /poicasi に一括置換"""
import json, sys, urllib.request

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
BASE = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

def get_all():
    req = urllib.request.Request(f"{BASE}?limit=100&fields=id,slug,content",
        headers={"X-MICROCMS-API-KEY": API_KEY})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())["contents"]

def patch(article_id, content):
    body = json.dumps({"content": content}, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(f"{BASE}/{article_id}", data=body,
        headers={"X-MICROCMS-API-KEY": API_KEY, "Content-Type": "application/json"},
        method="PATCH")
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

OLD = "https://poicasi.co.jp"
NEW = "/poicasi"

if __name__ == "__main__":
    articles = get_all()
    updated = 0
    for a in articles:
        content = a.get("content", "")
        if OLD in content:
            new_content = content.replace(OLD, NEW)
            # target="_blank" rel="noopener" も削除
            new_content = new_content.replace(
                f'href="{NEW}" target="_blank" rel="noopener"',
                f'href="{NEW}"'
            )
            patch(a["id"], new_content)
            print(f"[OK] {a['slug'][:50]}")
            updated += 1
    print(f"\n完了: {updated}件 更新")
