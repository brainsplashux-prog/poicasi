# -*- coding: utf-8 -*-
"""
ゲーム攻略記事バッチ投稿スクリプト（時給効率特化メディア）
選定基準: 報酬5,000円未満 x 7日以内達成 x 時給効率 = 報酬÷総時間
"""
import json
import sys
import urllib.request
import time

# Windows環境でのUTF-8出力設定
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"


def post_article(data):
    # microCMSの標準フィールドのみ送信（ゲーム専用カスタムフィールドは除外）
    ALLOWED_FIELDS = {"title", "slug", "description", "category", "articleType", "targetKeyword", "content", "publishedAt"}
    filtered = {k: v for k, v in data.items() if k in ALLOWED_FIELDS}

    body = json.dumps(filtered, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=body,
        headers={"X-MICROCMS-API-KEY": API_KEY, "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as res:
            result = json.loads(res.read())
            print(f"  [OK] 投稿成功: {data['title'][:40]}... (ID: {result.get('id','N/A')})")
            return result
    except urllib.error.HTTPError as e:
        err = e.read().decode('utf-8')
        print(f"  [NG] エラー ({e.code}): {err}")
        return None


# ===== ゲーム攻略記事データ =====
# 選定基準: 報酬<5000円 & 達成7日以内 & 時給効率高め
# 時給効率ランク: S=800円/h以上 / A=500-799 / B=300-499

GAME_GUIDE_ARTICLES = [

    # ===== G01: ライズオブキングダム =====
    {
        "title": "【ライズオブキングダム ポイ活攻略】3日で4,000円！時給600円の効率達成法",
        "slug": "rise-of-kingdoms-poikatsu-guide",
        "description": "ライズオブキングダムのポイ活攻略を完全解説。Moppyで4,000円案件を3日・約6.5時間で達成する方法。時給約615円のSランク効率ゲーム。日別ロードマップ付き。",
        "category": ["ゲーム攻略"],
        "articleType": ["game-guide"],
        "targetKeyword": "ライズオブキングダム ポイ活 攻略",
        "gameDifficulty": 2,
        "gameDaysToComplete": "3〜4日",
        "gameTotalHours": "約6.5時間",
        "gameMaxReward": 4000,
        "gameHourlyRate": 615,
        "gamePointSites": "Moppy,ポイントインカム,ハピタス",
        "content": """
<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item">
      <span class="game-summary-item__icon">⭐</span>
      <span class="game-summary-item__value">★★☆☆☆</span>
      <span class="game-summary-item__label">難易度</span>
    </div>
    <div class="game-summary-item">
      <span class="game-summary-item__icon">📅</span>
      <span class="game-summary-item__value">3〜4日</span>
      <span class="game-summary-item__label">達成日数</span>
    </div>
    <div class="game-summary-item">
      <span class="game-summary-item__icon">⏱️</span>
      <span class="game-summary-item__value">約6.5時間</span>
      <span class="game-summary-item__label">総プレイ時間</span>
    </div>
    <div class="game-summary-item game-summary-item--highlight">
      <span class="game-summary-item__icon">⚡</span>
      <span class="game-summary-item__value">約615円/時</span>
      <span class="game-summary-item__label">時給効率（Sランク）</span>
    </div>
  </div>
</div>

<p><strong>結論：ライズオブキングダムは最大4,000円を3〜4日・約6.5時間で達成できる、時給600円超えのSランク効率ゲームです。</strong>序盤の進め方さえ押さえれば、ゲーム経験ゼロでも達成できます。</p>

<h2>ポイントサイト別 報酬比較</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>4,000円</strong></td><td>城レベル9到達</td><td>約615円/時</td></tr>
<tr><td>ポイントインカム</td><td>3,500円</td><td>城レベル9到達</td><td>約538円/時</td></tr>
<tr><td>ハピタス</td><td>3,200円</td><td>城レベル9到達</td><td>約492円/時</td></tr>
</table>
<p>→ <strong>Moppyが最もお得</strong>。必ず事前に案件ページを確認してから始めよう。</p>

<h2>事前準備・注意事項</h2>
<div class="warning-box"><strong>⚠️ 必ず確認</strong><p>ポイントサイト経由でダウンロードすること。既存のアカウントや過去のインストール歴があると対象外になる場合があります。</p></div>
<ul>
<li>iOS / Android 両対応。新規インストールが条件</li>
<li>ダウンロード前にポイントサイトの案件ページを踏む（アフィリエイト計測が必要）</li>
<li>ATT（アプリのトラッキング許可）は「許可する」に設定</li>
</ul>

<h2>日別攻略ロードマップ</h2>
<div class="day-roadmap">
<div class="day-roadmap__title">3日間の攻略ステップ</div>

<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（約2時間）: 城レベル1〜5を一気に進める</h4>
    <p>チュートリアルをすべて完了→農場・採掘所・兵舎を最大まで建設→研究ツリーの「農業」を先行。序盤の資源収集クエストをひたすら消化。</p>
  </div>
</div>

<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2（約2.5時間）: 城レベル6〜8へ</h4>
    <p>各建物を城レベルに合わせて一斉アップグレード→同盟に加入（同盟ヘルプで建設速度UP）→宝石は建設速度アップのみに使用。無課金キープ。</p>
  </div>
</div>

<div class="day-step day-step--final">
  <div class="day-step__num">3</div>
  <div class="day-step__content">
    <h4>Day 3（約2時間）: 城レベル9達成 🎉</h4>
    <p>城レベル9へのアップグレード実行→ポイントサイトの管理画面で達成を確認→通常1〜2週間でポイント反映。</p>
  </div>
</div>
</div>

<h2>まとめ</h2>
<p>ライズオブキングダムは<strong>3日・6.5時間・時給615円</strong>という高効率案件。特にMoppyで達成すると4,000円と最高額。ゲーム自体も本格的で楽しく、ポイ活初心者にもおすすめのSランク案件です。</p>
<div class="cta-box"><div class="cta-box__title">ポイカジでも手軽にポイ活！</div><p class="cta-box__desc">30秒ゲームで毎日コツコツ貯める新感覚ポイ活も試してみて。</p><a href="https://poicasi.co.jp" class="cta-box__btn" target="_blank" rel="noopener">ポイカジを始める →</a></div>
""",
    },

    # ===== G02: ドラゴンシティ =====
    {
        "title": "【ドラゴンシティ ポイ活攻略】5日で3,500円！時給500円の達成手順を完全解説",
        "slug": "dragon-city-poikatsu-guide",
        "description": "ドラゴンシティのポイ活攻略を徹底解説。5日・約7時間でハッチング3体などの条件を達成し、最大3,500円を獲得する方法。時給約500円のAランク案件。",
        "category": ["ゲーム攻略"],
        "articleType": ["game-guide"],
        "targetKeyword": "ドラゴンシティ ポイ活 攻略",
        "gameDifficulty": 2,
        "gameDaysToComplete": "4〜5日",
        "gameTotalHours": "約7時間",
        "gameMaxReward": 3500,
        "gameHourlyRate": 500,
        "gamePointSites": "Moppy,ポイントインカム,モッピー",
        "content": """
<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★☆☆☆</span><span class="game-summary-item__label">難易度</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">4〜5日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約7時間</span><span class="game-summary-item__label">総プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約500円/時</span><span class="game-summary-item__label">時給効率（Aランク）</span></div>
  </div>
</div>

<p><strong>ドラゴンシティは放置育成ゲームの中でも達成しやすいポイ活案件です。</strong>ドラゴンを孵化させる（ハッチング）だけが主な条件で、待ち時間中は放置できるため実質プレイ時間は少なくて済みます。</p>

<h2>ポイントサイト別 報酬比較</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>3,500円</strong></td><td>ドラゴン3体孵化</td><td>約500円/時</td></tr>
<tr><td>ポイントインカム</td><td>3,000円</td><td>ドラゴン3体孵化</td><td>約429円/時</td></tr>
</table>

<h2>日別攻略ロードマップ</h2>
<div class="day-roadmap">
<div class="day-step"><div class="day-step__num">1</div><div class="day-step__content"><h4>Day 1: チュートリアル完了・農場拡張</h4><p>チュートリアルをすべてこなし、初期ドラゴン（炎）を孵化。農場を複数建設してゴールド収入を安定させる。</p></div></div>
<div class="day-step"><div class="day-step__num">2</div><div class="day-step__content"><h4>Day 2〜3: 2体目・3体目のドラゴン孵化</h4><p>育種所で属性違いのドラゴンを掛け合わせ→孵化待ち（数時間）→放置でOK。翌朝に確認するのがコツ。</p></div></div>
<div class="day-step day-step--final"><div class="day-step__num">4</div><div class="day-step__content"><h4>Day 4〜5: 3体目孵化で達成 🎉</h4><p>3体目のドラゴンが孵化したらポイントサイトで達成確認。ジェムは孵化時間短縮以外に使わない。</p></div></div>
</div>

<h2>まとめ</h2>
<p>ドラゴンシティは<strong>放置がメイン</strong>なので実質操作時間は少ない。Moppyなら3,500円・時給500円のAランク案件。放置ゲームが好きな方に特におすすめ。</p>
<div class="cta-box"><div class="cta-box__title">ポイカジでも手軽にポイ活！</div><p class="cta-box__desc">30秒ゲームで毎日コツコツ貯める新感覚ポイ活も試してみて。</p><a href="https://poicasi.co.jp" class="cta-box__btn" target="_blank" rel="noopener">ポイカジを始める →</a></div>
""",
    },

    # ===== G03: モンスターバスケット =====
    {
        "title": "【モンスターバスケット ポイ活攻略】7日で4,500円！時給480円の効率攻略",
        "slug": "monster-basket-poikatsu-guide",
        "description": "モンスターバスケットのポイ活攻略完全版。7日・約9時間でプレイヤーランク20到達。最大4,500円獲得、時給約480円のAランク案件。日別ロードマップ付き。",
        "category": ["ゲーム攻略"],
        "articleType": ["game-guide"],
        "targetKeyword": "モンスターバスケット ポイ活 攻略",
        "gameDifficulty": 3,
        "gameDaysToComplete": "5〜7日",
        "gameTotalHours": "約9時間",
        "gameMaxReward": 4500,
        "gameHourlyRate": 480,
        "gamePointSites": "Moppy,ポイントインカム,げん玉",
        "content": """
<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★★☆☆</span><span class="game-summary-item__label">難易度</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">5〜7日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約9時間</span><span class="game-summary-item__label">総プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約480円/時</span><span class="game-summary-item__label">時給効率（Aランク）</span></div>
  </div>
</div>

<p><strong>モンスターバスケットはランク20到達が条件の案件です。</strong>バトル系ゲームですが、序盤は難易度が低く、1日1〜2時間で着実に進められます。</p>

<h2>ポイントサイト別 報酬比較</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>4,500円</strong></td><td>プレイヤーランク20</td><td>約480円/時</td></tr>
<tr><td>ポイントインカム</td><td>4,000円</td><td>プレイヤーランク20</td><td>約444円/時</td></tr>
<tr><td>げん玉</td><td>3,800円</td><td>プレイヤーランク20</td><td>約422円/時</td></tr>
</table>

<h2>日別攻略ロードマップ</h2>
<div class="day-roadmap">
<div class="day-step"><div class="day-step__num">1</div><div class="day-step__content"><h4>Day 1（1.5時間）: チュートリアル〜ランク5</h4><p>チュートリアルを完了→デイリークエストをすべてこなす→スタミナが切れたら終了。無理せず翌日へ。</p></div></div>
<div class="day-step"><div class="day-step__num">2</div><div class="day-step__content"><h4>Day 2〜4（各1.5〜2時間）: ランク6〜15</h4><p>メインストーリーをひたすら進める→デイリークエスト毎日完走→スタミナ回復アイテムを惜しまず使う。</p></div></div>
<div class="day-step"><div class="day-step__num">5</div><div class="day-step__content"><h4>Day 5〜6（各1.5時間）: ランク16〜19</h4><p>このあたりから難易度が上がる。強化素材を集めてキャラを育成→無課金で十分進められる。</p></div></div>
<div class="day-step day-step--final"><div class="day-step__num">7</div><div class="day-step__content"><h4>Day 7（1時間）: ランク20達成 🎉</h4><p>ランク20に到達→ポイントサイトの達成確認→反映まで通常1〜2週間。</p></div></div>
</div>

<h2>まとめ</h2>
<p>Moppyで4,500円・時給480円のAランク案件。バトル系が好きなら特に楽しみながら達成できる。7日ギリギリになりやすいので早めにスタートを。</p>
<div class="cta-box"><div class="cta-box__title">ポイカジでも手軽にポイ活！</div><p class="cta-box__desc">30秒ゲームで毎日コツコツ貯める新感覚ポイ活。</p><a href="https://poicasi.co.jp" class="cta-box__btn" target="_blank" rel="noopener">ポイカジを始める →</a></div>
""",
    },
]


if __name__ == "__main__":
    print("=" * 60)
    print("ゲーム攻略記事 バッチ投稿スクリプト（時給効率特化）")
    print(f"投稿予定: {len(GAME_GUIDE_ARTICLES)} 記事")
    print("=" * 60)
    print()

    success = 0
    fail = 0
    for i, article in enumerate(GAME_GUIDE_ARTICLES, 1):
        print(f"[{i}/{len(GAME_GUIDE_ARTICLES)}] 投稿中: {article['title'][:40]}...")
        result = post_article(article)
        if result:
            success += 1
        else:
            fail += 1
        time.sleep(1)  # APIレート制限対策

    print()
    print(f"完了: 成功 {success}件 / 失敗 {fail}件")
