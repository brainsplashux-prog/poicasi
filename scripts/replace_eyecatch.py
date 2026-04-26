# -*- coding: utf-8 -*-
"""新しいアイキャッチ画像を公開ディレクトリにコピーし、microCMS記事のcontent内の画像URLを差し替える"""
import json
import urllib.request
import os
import re
import shutil
import time
import glob

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ARTICLES_ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"
SITE_URL = "https://media.poicasi.co.jp"

# 新画像のソースディレクトリ
NEW_IMAGE_DIR = r"C:\Users\dyesi\.gemini\antigravity\brain\8fd02cc1-ead1-4569-854a-da33fd25b97f"
# 公開用ディレクトリ
PUBLIC_EYECATCH_DIR = r"C:\Users\dyesi\OneDrive\Desktop\Roundup\poicasi-site\public\eyecatch"

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
        # 最新のものを選択
        return max(files, key=os.path.getmtime)
    return None


def find_old_image(prefix):
    """既存の画像ファイルを検索"""
    pattern = os.path.join(PUBLIC_EYECATCH_DIR, f"{prefix}_*.png")
    files = glob.glob(pattern)
    if files:
        return files[0]
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
    
    print(f"=== アイキャッチ画像差し替え開始 ({total}記事) ===\n")
    
    for i, (article_id, (image_prefix, alt_text)) in enumerate(ARTICLE_IMAGE_MAP.items(), 1):
        print(f"[{i}/{total}] {article_id} ({image_prefix})")
        
        # Step 1: 新画像を見つける
        new_image_path = find_new_image(image_prefix)
        if not new_image_path:
            results.append(f"SKIP: {article_id} - new image not found: {image_prefix}")
            print(f"  ❌ New image not found: {image_prefix}")
            continue
        
        new_image_filename = os.path.basename(new_image_path)
        print(f"  New image: {new_image_filename}")
        
        # Step 2: 既存画像のファイル名を取得
        old_image_path = find_old_image(image_prefix)
        old_image_filename = os.path.basename(old_image_path) if old_image_path else None
        
        # Step 3: 新画像をpublic/eyecatchにコピー
        dest_path = os.path.join(PUBLIC_EYECATCH_DIR, new_image_filename)
        shutil.copy2(new_image_path, dest_path)
        print(f"  Copied to public/eyecatch/")
        
        # Step 4: microCMS記事のcontent内のimg srcを差し替える
        try:
            content = get_article_content(article_id)
        except Exception as e:
            results.append(f"FAIL_GET: {article_id} - {str(e)[:100]}")
            print(f"  ❌ Failed to get content: {e}")
            continue
        
        # 旧画像URLのパターンを探して新しいURLに差し替え
        old_url_pattern = f"/eyecatch/{image_prefix}_"
        new_image_url = f"{SITE_URL}/eyecatch/{new_image_filename}"
        
        if old_url_pattern in content:
            # 旧URLを正規表現で新URLに書き換え
            new_content = re.sub(
                rf'(src="[^"]*)/eyecatch/{re.escape(image_prefix)}_[^"]*\.png"',
                f'src="{new_image_url}"',
                content
            )
            
            if new_content != content:
                print(f"  Updating microCMS content...")
                success = update_article_content(article_id, new_content)
                if success:
                    results.append(f"OK: {article_id} - {new_image_filename}")
                    print(f"  ✅ Done!")
                else:
                    results.append(f"FAIL_UPDATE: {article_id}")
                    print(f"  ❌ Update failed")
            else:
                results.append(f"NO_CHANGE: {article_id} - regex didn't match")
                print(f"  ⚠️ No regex match in content")
        else:
            results.append(f"NO_OLD_URL: {article_id} - old URL pattern not found")
            print(f"  ⚠️ Old eyecatch URL not found in content")
        
        time.sleep(0.5)  # rate limit
    
    # Step 5: 古い画像を削除（オプション）
    print("\n--- 古い画像のクリーンアップ ---")
    for article_id, (image_prefix, alt_text) in ARTICLE_IMAGE_MAP.items():
        old_path = find_old_image(image_prefix)
        new_path = find_new_image(image_prefix)
        if old_path and new_path:
            old_name = os.path.basename(old_path)
            new_name = os.path.basename(new_path)
            if old_name != new_name:
                try:
                    os.remove(old_path)
                    print(f"  Removed old: {old_name}")
                except Exception as e:
                    print(f"  Failed to remove {old_name}: {e}")
    
    # 結果を保存
    with open("c:/tmp/eyecatch_replace_results.txt", "w", encoding="utf-8") as f:
        for r in results:
            f.write(r + "\n")
    
    ok_count = sum(1 for r in results if r.startswith("OK"))
    print(f"\n=== 完了! {ok_count}/{total} 成功 ===")
    print(f"結果: c:/tmp/eyecatch_replace_results.txt")


if __name__ == "__main__":
    main()
