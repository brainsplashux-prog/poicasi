# -*- coding: utf-8 -*-
"""画像URLの動作確認→microCMS記事contentをhp.poicasi.co.jpのURLに差し替え"""
import json
import urllib.request
import re
import time

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ARTICLES_ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

# 新しいベースURL (S3→CloudFront)
NEW_BASE_URL = "https://hp.poicasi.co.jp/eyecatch"

# 記事ID → (画像ファイル名, alt text)
ARTICLE_IMAGE_MAP = {
    "vwue-yktf5b": ("eyecatch_ranking_1775093010942.png", "稼ぎやすくて面白いポイ活アプリランキング"),
    "ov_wulfvt-j": ("eyecatch_new_methods_1775093026222.png", "2026年の新しいポイ活の稼ぎ方"),
    "wvmlaa632y": ("eyecatch_bored_1775093040359.png", "ポイ活に飽きた時の解決策"),
    "a-ukptguru": ("eyecatch_mendokusai_1775093070719.png", "めんどくさくないポイ活の選び方"),
    "kttvo5pw46l": ("eyecatch_tired_1775093084086.png", "疲れないポイ活の選び方"),
    "x-n4hfk5a1": ("eyecatch_dl_vs_jousetsu_1775093097890.png", "DL型vs常設ゲーム型の比較"),
    "m7mju2ms0u3f": ("eyecatch_same_app_1775093129849.png", "同じゲームでずっと稼ぐポイ活"),
    "jhxfm78-p8": ("eyecatch_storage_1775093142850.png", "容量を圧迫しないポイ活ゲーム"),
    "4xz14_booa": ("eyecatch_kakin_1775093156984.png", "無課金で稼げるポイ活ゲーム"),
    "7gnhw56z3": ("eyecatch_checklist_1775093185268.png", "ゲームDL型ポイ活の案件チェックリスト"),
    "cv1gt_z69bl": ("eyecatch_waste_time_1775093200158.png", "ポイ活ゲームの時間効率"),
    "3vx7_je8da5": ("eyecatch_demerit_1775093213118.png", "ポイ活ゲームのデメリット"),
    "gdqfapzehq": ("eyecatch_dl_vs_jousetsu2_1775093247085.png", "DL型と常設型の違い解説"),
    "wn-qha-b6r": ("eyecatch_fun_never_boring_1775093263572.png", "飽きないポイ活アプリの選び方"),
    "iwuf3rpw56n": ("eyecatch_continue_tips_1775093279087.png", "ポイ活が続かない人の共通点"),
    "ocalldyky1": ("eyecatch_high_value_after_1775093311075.png", "高額案件の弾切れ後の戦略"),
    "ffyq1e0hkg": ("eyecatch_high_value_guide_1775093327295.png", "高額ポイ活案件の完全ガイド"),
    "1mj8yl-vaw5": ("eyecatch_efficiency_ranking_1775093345392.png", "ポイ活ゲームの効率ランキング"),
    "0pdeqsc6m": ("eyecatch_app_top20_1775093374392.png", "ポイ活ゲームアプリTOP20"),
    "831re6tu5": ("eyecatch_risk_safety_1775093390265.png", "ポイ活の危険性検証と安全な利用法"),
    "pft2gedmk99": ("eyecatch_point_exchange_1775093405554.png", "ポイント交換先ガイド"),
    "fk2dranzkhg": ("eyecatch_earning_manual_1775093441592.png", "ポイ活の稼ぎ方完全マニュアル"),
    "0dgt_fslqpoh": ("eyecatch_beginner_roadmap_1775093458019.png", "ポイ活初心者ロードマップ"),
    "658aonzbm7u": ("eyecatch_poicasi_howto_1775093472991.png", "ポイカジの始め方と攻略法"),
    "8321cbrkqa": ("eyecatch_3app_comparison_1775093523465.png", "3大ゲームポイ活アプリ比較"),
    "6y_9l3-nb186": ("eyecatch_complete_guide_1775093538459.png", "ゲームポイ活アプリ完全ガイド"),
}

# Step 1: URLアクセスチェック
print("=== Step 1: URLアクセスチェック ===")
test_url = f"{NEW_BASE_URL}/{list(ARTICLE_IMAGE_MAP.values())[0][0]}"
print(f"Testing: {test_url}")
try:
    req = urllib.request.Request(test_url, method="HEAD")
    with urllib.request.urlopen(req) as res:
        print(f"✅ HTTP {res.status} - Image accessible!")
except Exception as e:
    print(f"❌ Error: {e}")
    print("CloudFrontのキャッシュ無効化が必要かもしれません。")
    print("Proceeding anyway - updating content URLs...")

# Step 2: microCMS記事の差し替え
print(f"\n=== Step 2: microCMS記事content差し替え ({len(ARTICLE_IMAGE_MAP)}記事) ===\n")

results = []
for i, (article_id, (new_filename, alt_text)) in enumerate(ARTICLE_IMAGE_MAP.items(), 1):
    print(f"[{i}/{len(ARTICLE_IMAGE_MAP)}] {article_id}")
    
    new_url = f"{NEW_BASE_URL}/{new_filename}"
    
    # 記事のcontent取得
    try:
        req = urllib.request.Request(
            f"{ARTICLES_ENDPOINT}/{article_id}?fields=content",
            headers={"X-MICROCMS-API-KEY": API_KEY},
        )
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read())
            content = data.get("content", "")
    except Exception as e:
        results.append(f"FAIL_GET: {article_id} - {e}")
        print(f"  ❌ Failed to get content")
        continue
    
    # content内のeyecatch画像URLを差し替え
    # パターン: <img src="何らかのURL/eyecatch_xxx.png" で始まるimgタグ
    pattern = re.compile(r'(<img[^>]*\bsrc=")([^"]*eyecatch_[^"]*\.png)(")')
    match = pattern.search(content)
    
    if match:
        old_url = match.group(2)
        new_content = pattern.sub(
            lambda m: f'{m.group(1)}{new_url}{m.group(3)}',
            content,
            count=1
        )
        
        if new_content != content:
            # PATCH
            patch_data = json.dumps({"content": new_content}).encode("utf-8")
            req = urllib.request.Request(
                f"{ARTICLES_ENDPOINT}/{article_id}",
                data=patch_data,
                headers={
                    "X-MICROCMS-API-KEY": API_KEY,
                    "Content-Type": "application/json",
                },
                method="PATCH",
            )
            try:
                with urllib.request.urlopen(req) as res:
                    results.append(f"OK: {article_id} | {old_url} -> {new_url}")
                    print(f"  ✅ {old_url[:50]}... -> {new_url[:50]}...")
            except urllib.error.HTTPError as e:
                err = e.read().decode("utf-8")
                results.append(f"FAIL_UPDATE: {article_id} - {e.code}")
                print(f"  ❌ Update failed: {e.code}")
        else:
            results.append(f"ALREADY_OK: {article_id} - URL already correct")
            print(f"  ✅ Already correct")
    else:
        results.append(f"NO_MATCH: {article_id} - no eyecatch img in content")
        print(f"  ⚠️ No eyecatch img found")
    
    time.sleep(0.5)

# 結果保存
with open("c:/tmp/final_replace_results.txt", "w", encoding="utf-8") as f:
    for r in results:
        f.write(r + "\n")

ok = sum(1 for r in results if r.startswith("OK") or r.startswith("ALREADY"))
print(f"\n=== 完了! {ok}/{len(ARTICLE_IMAGE_MAP)} 成功 ===")
print(f"結果: c:/tmp/final_replace_results.txt")
