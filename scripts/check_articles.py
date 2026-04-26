# -*- coding: utf-8 -*-
import json
import urllib.request

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"

url = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles?limit=20"
req = urllib.request.Request(url, headers={"X-MICROCMS-API-KEY": API_KEY})
with urllib.request.urlopen(req) as res:
    data = json.loads(res.read())

with open("c:/tmp/articles_list.txt", "w", encoding="utf-8") as f:
    for a in data["contents"]:
        slug = a.get("slug", "?")
        cid = a["id"]
        status = "PUB" if a.get("publishedAt") else "DRAFT"
        f.write(f"{slug} => {cid} [{status}]\n")
    f.write(f"\nTotal: {len(data['contents'])} articles\n")

print("Done - output written to c:/tmp/articles_list.txt")
