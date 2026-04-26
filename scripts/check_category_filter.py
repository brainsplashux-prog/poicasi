# -*- coding: utf-8 -*-
import json, urllib.request
from urllib.parse import quote

API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
BASE = "https://07lzrpng23.microcms.io/api/v1/articles"

cats = ["ゲーム×ポイ活", "ポイ活入門", "ポイ活比較", "ポイント交換", "安全性"]
for cat in cats:
    url = f"{BASE}?limit=1&filters=category%5Bcontains%5D{quote(cat)}"
    req = urllib.request.Request(url, headers={"X-MICROCMS-API-KEY": API_KEY})
    with urllib.request.urlopen(req) as r:
        d = json.loads(r.read())
        print(f"[{cat}] contains -> {d['totalCount']}件")
