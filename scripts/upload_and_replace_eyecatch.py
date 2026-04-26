# -*- coding: utf-8 -*-
"""
新アイキャッチ画像をmicroCMS管理APIにアップロードし、
記事contentの画像URLをmicroCMS配信URLに差し替えるスクリプト
"""
import json
import urllib.request
import os
import re
import time
import glob

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ARTICLES_ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"
MEDIA_ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms-management.io/api/v1/media"

# 新画像のソースディレクトリ
NEW_IMAGE_DIR = r"C:\Users\dyesi\.gemini\antigravity\brain\8fd02cc1-ead1-4569-854a-da33fd25b97f"

# 記事ID → (画像プレフィックス, alt text) のマッピング
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


def find_new_image(prefix):
    """新しい画像ファイルを検索"""
    pattern = os.path.join(NEW_IMAGE_DIR, f"{prefix}_*.png")
    files = glob.glob(pattern)
    if files:
        return max(files, key=os.path.getmtime)
    return None


def upload_image_to_microcms(filepath):
    """microCMS管理APIで画像をアップロード"""
    filename = os.path.basename(filepath)
    
    with open(filepath, "rb") as f:
        image_data = f.read()
    
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
        print(f"  Content update failed: {e.code} - {error_body[:200]}")
        return False


def main():
    results = []
    total = len(ARTICLE_IMAGE_MAP)
    
    print(f"=== microCMSアップロード＆画像差し替え ({total}記事) ===\n")
    
    for i, (article_id, (image_prefix, alt_text)) in enumerate(ARTICLE_IMAGE_MAP.items(), 1):
        print(f"[{i}/{total}] {article_id} ({image_prefix})")
        
        # Step 1: 新画像を見つける
        new_image_path = find_new_image(image_prefix)
        if not new_image_path:
            results.append(f"SKIP: {article_id} - new image not found: {image_prefix}")
            print(f"  ❌ New image not found")
            continue
        
        print(f"  📁 Found: {os.path.basename(new_image_path)}")
        
        # Step 2: microCMSにアップロード
        print(f"  📤 Uploading to microCMS...")
        uploaded_url = upload_image_to_microcms(new_image_path)
        if not uploaded_url:
            results.append(f"FAIL_UPLOAD: {article_id} - {image_prefix}")
            print(f"  ❌ Upload failed")
            continue
        
        print(f"  ✅ Uploaded: {uploaded_url}")
        
        # Step 3: 記事のcontentを取得
        try:
            content = get_article_content(article_id)
        except Exception as e:
            results.append(f"FAIL_GET: {article_id} - {str(e)[:100]}")
            print(f"  ❌ Failed to get content")
            continue
        
        # Step 4: content内の最初の<img>タグのsrcを差し替え
        # 既存の eyecatch 画像URLパターンを探す
        old_pattern = re.compile(r'(<img[^>]*src=")([^"]*eyecatch[^"]*\.png)("[^>]*>)')
        match = old_pattern.search(content)
        
        if match:
            old_img_tag = match.group(0)
            # 新しいimg tagを構築（srcのみ変更、他のattributesは保持）
            new_img_tag = old_pattern.sub(
                lambda m: f'{m.group(1)}{uploaded_url}{m.group(3)}',
                content,
                count=1  # 最初の1つだけ差し替え
            )
            
            if new_img_tag != content:
                print(f"  📝 Updating content with new URL...")
                success = update_article_content(article_id, new_img_tag)
                if success:
                    results.append(f"OK: {article_id} -> {uploaded_url}")
                    print(f"  ✅ Done!")
                else:
                    results.append(f"FAIL_UPDATE: {article_id}")
                    print(f"  ❌ Content update failed")
            else:
                results.append(f"NO_CHANGE: {article_id}")
                print(f"  ⚠️ No change in content")
        else:
            # eyecatch URLがないが、他のimgタグがあるかもしれない
            # media.poicasi.co.jpのURLも探す
            alt_pattern = re.compile(r'(<img[^>]*src=")([^"]*)(eyecatch_[^"]*\.png)("[^>]*>)')
            alt_match = alt_pattern.search(content)
            if alt_match:
                new_content = alt_pattern.sub(
                    lambda m: f'{m.group(1)}{uploaded_url}{m.group(4)}',
                    content,
                    count=1
                )
                print(f"  📝 Updating content (alt pattern)...")
                success = update_article_content(article_id, new_content)
                if success:
                    results.append(f"OK: {article_id} -> {uploaded_url}")
                    print(f"  ✅ Done!")
                else:
                    results.append(f"FAIL_UPDATE: {article_id}")
            else:
                results.append(f"NO_MATCH: {article_id} - no eyecatch img found in content")
                print(f"  ⚠️ No eyecatch img found in content")
        
        time.sleep(1)  # rate limit (管理APIは厳しめ)
    
    # 結果を保存
    with open("c:/tmp/eyecatch_upload_replace_results.txt", "w", encoding="utf-8") as f:
        for r in results:
            f.write(r + "\n")
    
    ok_count = sum(1 for r in results if r.startswith("OK"))
    fail_count = sum(1 for r in results if "FAIL" in r)
    print(f"\n=== 完了! {ok_count}/{total} 成功, {fail_count} 失敗 ===")
    print(f"結果: c:/tmp/eyecatch_upload_replace_results.txt")


if __name__ == "__main__":
    main()
