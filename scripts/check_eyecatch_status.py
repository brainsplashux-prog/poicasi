# -*- coding: utf-8 -*-
"""全記事のeyecatch状態とcontent内のimg状態を確認"""
import json
import urllib.request

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"

url = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles?limit=50&fields=id,title,slug,eyecatch,content,publishedAt&orders=-publishedAt"
req = urllib.request.Request(url, headers={"X-MICROCMS-API-KEY": API_KEY})
with urllib.request.urlopen(req) as res:
    data = json.loads(res.read())

output = []
for a in data["contents"]:
    status = "PUB" if a.get("publishedAt") else "DRF"
    eyecatch = a.get("eyecatch")
    has_eyecatch_field = "YES" if eyecatch else "NO"
    
    content = a.get("content", "")
    has_img = "<img" in content
    
    # Check if content starts with eyecatch img
    img_src = ""
    if has_img:
        import re
        match = re.search(r'<img[^>]+src="([^"]+)"', content[:500])
        if match:
            img_src = match.group(1)[:80]
    
    output.append(f"[{status}] {a['id']}")
    output.append(f"  Title: {a['title'][:60]}")
    output.append(f"  Slug: {a.get('slug','?')}")
    output.append(f"  Eyecatch field: {has_eyecatch_field}")
    if eyecatch:
        eyecatch_url = eyecatch if isinstance(eyecatch, str) else eyecatch.get("url", "?")
        output.append(f"  Eyecatch URL: {eyecatch_url[:80]}")
    output.append(f"  Content has img: {has_img}")
    if img_src:
        output.append(f"  First img src: {img_src}")
    output.append("")

with open("c:/tmp/eyecatch_status.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print(f"Done - {len(data['contents'])} articles checked. See c:/tmp/eyecatch_status.txt")
