# -*- coding: utf-8 -*-
import json, urllib.request

ENDPOINT = "https://07lzrpng23.microcms.io/api/v1/articles"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"

req = urllib.request.Request(
    ENDPOINT + "?limit=50&fields=id,title,slug,category,publishedAt&orders=-publishedAt",
    headers={"X-MICROCMS-API-KEY": API_KEY},
)
with urllib.request.urlopen(req) as res:
    data = json.loads(res.read())

lines = []
for a in data["contents"]:
    status = "PUB" if a.get("publishedAt") else "DRF"
    cat = a.get("category", "N/A")
    if isinstance(cat, list):
        cat = cat[0] if cat else "N/A"
    slug = a.get("slug", "?")
    title = a.get("title", "?")[:60]
    aid = a.get("id", "?")
    lines.append(f"{status} | {aid} | {slug} | {cat} | {title}")

lines.append(f"\nTotal: {data['totalCount']}")

with open("c:/tmp/article_list.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("Done - saved to c:/tmp/article_list.txt")
