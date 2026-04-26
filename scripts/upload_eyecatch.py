# -*- coding: utf-8 -*-
"""アイキャッチ画像をmicroCMSにアップロードし、各記事に紐付けるスクリプト"""
import json
import urllib.request
import os
import base64
import time

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ARTICLES_ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"
MEDIA_ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms-management.io/api/v1/media"

IMAGE_DIR = r"C:\Users\dyesi\.gemini\antigravity\brain\c6adc3b6-c38b-49dc-82d4-7c4ea57965f5"

# 記事ID → 画像ファイルのマッピング
ARTICLE_IMAGE_MAP = {
    # Batch 5b: ランキング、新しい稼ぎ方
    "vwue-yktf5b": "eyecatch_ranking",           # 稼ぎやすくて面白いランキング
    "ov_wulfvt-j": "eyecatch_new_methods",        # 新しい稼ぎ方5選
    # Batch 5a: 飽きた、めんどくさい、疲れた
    "wvmlaa632y": "eyecatch_bored",               # ポイ活に飽きた
    "a-ukptguru": "eyecatch_mendokusai",          # ポイ活がめんどくさい
    "kttvo5pw46l": "eyecatch_tired",              # ポイ活に疲れた
    # Batch 4: DL型 vs 常設型（比較表）
    "x-n4hfk5a1": "eyecatch_dl_vs_jousetsu",      # DL型vs常設型 比較表
    # Batch 3: ゲーム系記事
    "m7mju2ms0u3f": "eyecatch_same_app",          # 同じゲームでずっと稼ぐ
    "jhxfm78-p8": "eyecatch_storage",             # 容量圧迫しない
    "4xz14_booa": "eyecatch_kakin",               # 課金は必要？
    "7gnhw56z3": "eyecatch_checklist",            # 案件選び7つのチェック
    "cv1gt_z69bl": "eyecatch_waste_time",         # 時間の無駄？
    "3vx7_je8da5": "eyecatch_demerit",            # デメリット5選
    # Batch 2: 選び方・楽しさ
    "gdqfapzehq": "eyecatch_dl_vs_jousetsu2",     # DL型vs常設型（解説版）
    "wn-qha-b6r": "eyecatch_fun_never_boring",    # 楽しすぎて止められない
    "iwuf3rpw56n": "eyecatch_continue_tips",       # 続かない人の共通点
    "ocalldyky1": "eyecatch_high_value_after",     # 高額弾切れ後
    "ffyq1e0hkg": "eyecatch_high_value_guide",     # 高額完全ガイド
    "1mj8yl-vaw5": "eyecatch_efficiency_ranking",  # 効率ランキング
    # Batch 1: 基本記事
    "0pdeqsc6m": "eyecatch_app_top20",            # TOP20ランキング
    "831re6tu5": "eyecatch_risk_safety",           # 危険性検証
    "pft2gedmk99": "eyecatch_point_exchange",      # ポイント交換ガイド
    "fk2dranzkhg": "eyecatch_earning_manual",      # 稼ぎ方完全マニュアル
    "0dgt_fslqpoh": "eyecatch_beginner_roadmap",   # 初心者ロードマップ
    "658aonzbm7u": "eyecatch_poicasi_howto",       # ポイカジ攻略法
    "8321cbrkqa": "eyecatch_3app_comparison",      # 3アプリ比較
    "6y_9l3-nb186": "eyecatch_complete_guide",     # 完全ガイド
}


def find_image_file(image_name):
    """画像ファイルを検索（タイムスタンプ付きファイル名に対応）"""
    for f in os.listdir(IMAGE_DIR):
        if f.startswith(image_name) and f.endswith(".png"):
            return os.path.join(IMAGE_DIR, f)
    return None


def upload_image_to_microcms(filepath):
    """microCMS管理APIで画像をアップロード"""
    filename = os.path.basename(filepath)
    
    with open(filepath, "rb") as f:
        image_data = f.read()
    
    # multipart/form-data でアップロード
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
        f"Content-Type: image/png\r\n\r\n"
    ).encode("utf-8") + image_data + f"\r\n--{boundary}--\r\n".encode("utf-8")
    
    req = urllib.request.Request(
        MEDIA_ENDPOINT,
        data=body,
        headers={
            "X-MICROCMS-API-KEY": API_KEY,
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
        method="POST",
    )
    
    try:
        with urllib.request.urlopen(req) as res:
            result = json.loads(res.read())
            return result.get("url")
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"  Upload failed: {e.code} - {error_body[:200]}")
        return None


def update_article_eyecatch(article_id, image_url):
    """記事のeyecatchフィールドを更新"""
    data = json.dumps({"eyecatch": image_url}).encode("utf-8")
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
    
    for i, (article_id, image_name) in enumerate(ARTICLE_IMAGE_MAP.items(), 1):
        print(f"[{i}/{total}] {article_id} -> {image_name}")
        
        # 画像ファイルを探す
        filepath = find_image_file(image_name)
        if not filepath:
            results.append(f"SKIP: {article_id} - image not found: {image_name}")
            print(f"  Image not found: {image_name}")
            continue
        
        # microCMSにアップロード
        print(f"  Uploading {os.path.basename(filepath)}...")
        image_url = upload_image_to_microcms(filepath)
        if not image_url:
            results.append(f"FAIL_UPLOAD: {article_id} - {image_name}")
            continue
        
        print(f"  Uploaded: {image_url}")
        
        # 記事のeyecatchを更新
        print(f"  Updating article eyecatch...")
        success = update_article_eyecatch(article_id, image_url)
        if success:
            results.append(f"OK: {article_id} - {image_name} -> {image_url}")
            print(f"  Done!")
        else:
            results.append(f"FAIL_UPDATE: {article_id} - {image_name}")
        
        time.sleep(0.5)  # rate limit
    
    # 結果をファイルに保存
    with open("c:/tmp/eyecatch_upload_results.txt", "w", encoding="utf-8") as f:
        for r in results:
            f.write(r + "\n")
    
    ok_count = sum(1 for r in results if r.startswith("OK"))
    print(f"\nDone! {ok_count}/{total} succeeded. Results in c:/tmp/eyecatch_upload_results.txt")


if __name__ == "__main__":
    main()
