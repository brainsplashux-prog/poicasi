# -*- coding: utf-8 -*-
"""各記事のcontentにアイキャッチ画像を挿入するスクリプト"""
import json
import urllib.request
import os
import time
import glob

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ARTICLES_ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"
SITE_URL = "https://media.poicasi.co.jp"
IMAGE_DIR = r"c:\Users\dyesi\OneDrive\Desktop\Roundup\poicasi-site\public\eyecatch"

# 記事ID → 画像名プレフィックスのマッピング
ARTICLE_IMAGE_MAP = {
    "vwue-yktf5b": ("eyecatch_ranking", "稼ぎやすくて面白いポイ活アプリランキング"),
    "ov_wulfvt-j": ("eyecatch_new_methods", "2026年の新しいポイ活の稼ぎ方"),
    "wvmlaa632y": ("eyecatch_bored", "ポイ活に飽きた時の解決策"),
    "a-ukptguru": ("eyecatch_mendokusai", "めんどくさくないポイ活の選び方"),
    "kttvo5pw46l": ("eyecatch_tired", "疲れないポイ活の選び方"),
    "x-n4hfk5a1": ("eyecatch_dl_vs_jousetsu", "DL型vs常設ゲーム型の比較"),
    "m7mju2ms0u3f": ("eyecatch_same_app", "同じゲームでずっと稼ぐポイ活"),
    "jhxfm78-p8": ("eyecatch_storage", "容量を圧迫しないポイ活ゲーム"),
    "4xz14_booa": ("eyecatch_kakin", "無課金で稼げるポイ活ゲーム"),
    "7gnhw56z3": ("eyecatch_checklist", "ゲームDL型ポイ活の案件チェックリスト"),
    "cv1gt_z69bl": ("eyecatch_waste_time", "ポイ活ゲームの時間効率"),
    "3vx7_je8da5": ("eyecatch_demerit", "ポイ活ゲームのデメリット"),
    "gdqfapzehq": ("eyecatch_dl_vs_jousetsu2", "DL型と常設型の違い解説"),
    "wn-qha-b6r": ("eyecatch_fun_never_boring", "飽きないポイ活アプリの選び方"),
    "iwuf3rpw56n": ("eyecatch_continue_tips", "ポイ活が続かない人の共通点"),
    "ocalldyky1": ("eyecatch_high_value_after", "高額案件の弾切れ後の戦略"),
    "ffyq1e0hkg": ("eyecatch_high_value_guide", "高額ポイ活案件の完全ガイド"),
    "1mj8yl-vaw5": ("eyecatch_efficiency_ranking", "ポイ活ゲームの効率ランキング"),
    "0pdeqsc6m": ("eyecatch_app_top20", "ポイ活ゲームアプリTOP20"),
    "831re6tu5": ("eyecatch_risk_safety", "ポイ活の危険性検証と安全な利用法"),
    "pft2gedmk99": ("eyecatch_point_exchange", "ポイント交換先ガイド"),
    "fk2dranzkhg": ("eyecatch_earning_manual", "ポイ活の稼ぎ方完全マニュアル"),
    "0dgt_fslqpoh": ("eyecatch_beginner_roadmap", "ポイ活初心者ロードマップ"),
    "658aonzbm7u": ("eyecatch_poicasi_howto", "ポイカジの始め方と攻略法"),
    "8321cbrkqa": ("eyecatch_3app_comparison", "3大ゲームポイ活アプリ比較"),
    "6y_9l3-nb186": ("eyecatch_complete_guide", "ゲームポイ活アプリ完全ガイド"),
}


def find_image_filename(prefix):
    """publicフォルダから画像ファイル名を取得"""
    pattern = os.path.join(IMAGE_DIR, f"{prefix}_*.png")
    files = glob.glob(pattern)
    if files:
        return os.path.basename(files[0])
    return None


def get_article_content(article_id):
    """記事のcontentを取得"""
    req = urllib.request.Request(
        f"{ARTICLES_ENDPOINT}/{article_id}?fields=content",
        headers={"X-MICROCMS-API-KEY": API_KEY},
    )
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read())
        return data.get("content", "")


def update_article_content(article_id, new_content):
    """記事のcontentを更新"""
    data = json.dumps({"content": new_content}).encode("utf-8")
    req = urllib.request.Request(
        f"{ARTICLES_ENDPOINT}/{article_id}",
        data=data,
        headers={
            "X-MICROCMS-API-KEY": API_KEY,
            "Content-Type": "application/json",
        },
        method="PATCH",
    )
    try:
        with urllib.request.urlopen(req) as res:
            return True
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"  Update failed: {e.code} - {error_body[:200]}")
        return False


def main():
    results = []
    total = len(ARTICLE_IMAGE_MAP)
    
    for i, (article_id, (image_prefix, alt_text)) in enumerate(ARTICLE_IMAGE_MAP.items(), 1):
        print(f"[{i}/{total}] {article_id}")
        
        # 画像ファイル名を取得
        image_filename = find_image_filename(image_prefix)
        if not image_filename:
            results.append(f"SKIP: {article_id} - image not found: {image_prefix}")
            print(f"  Image not found: {image_prefix}")
            continue
        
        image_url = f"{SITE_URL}/eyecatch/{image_filename}"
        image_tag = f'<img src="{image_url}" alt="{alt_text}" width="1200" height="630" style="width:100%;border-radius:12px;margin-bottom:24px;" />'
        
        # 現在のcontentを取得
        try:
            content = get_article_content(article_id)
        except Exception as e:
            results.append(f"FAIL_GET: {article_id} - {str(e)[:100]}")
            print(f"  Failed to get content: {e}")
            continue
        
        # すでに画像が挿入されていたらスキップ
        if "/eyecatch/" in content:
            results.append(f"SKIP_EXISTS: {article_id} - already has eyecatch")
            print(f"  Already has eyecatch, skipping")
            continue
        
        # contentの先頭にアイキャッチ画像を挿入
        new_content = image_tag + "\n\n" + content
        
        # 更新
        print(f"  Updating with {image_filename}...")
        success = update_article_content(article_id, new_content)
        if success:
            results.append(f"OK: {article_id} - {image_filename}")
            print(f"  Done!")
        else:
            results.append(f"FAIL_UPDATE: {article_id}")
        
        time.sleep(0.5)
    
    # 結果を保存
    with open("c:/tmp/eyecatch_insert_results.txt", "w", encoding="utf-8") as f:
        for r in results:
            f.write(r + "\n")
    
    ok_count = sum(1 for r in results if r.startswith("OK"))
    print(f"\nDone! {ok_count}/{total} succeeded. Results in c:/tmp/eyecatch_insert_results.txt")


if __name__ == "__main__":
    main()
