# -*- coding: utf-8 -*-
"""ビビッドアーミー 詳細版投稿"""
import json, sys, urllib.request
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

CONTENT = """<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★☆☆☆</span><span class="game-summary-item__label">難易度（初心者OK）</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">3〜5日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約6時間</span><span class="game-summary-item__label">実質プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約583円/時</span><span class="game-summary-item__label">時給効率（Aランク）</span></div>
  </div>
</div>

<p><strong>この記事を読めばわかること：</strong>ビビッドアーミーを初めてプレイする方でも、3〜5日・約6時間でMoppyで最大3,500円を獲得できます。城レベル（本部レベル）を指定レベルまで上げる手順を操作レベルで解説します。</p>

<div class="warning-box"><strong>⚠️ 始める前に必ず確認</strong><p>ポイントサイトの案件ページを経由してからダウンロードしてください。達成条件（本部レベルなど）は案件によって異なります。</p></div>

<h2>ポイントサイト別 報酬比較（2026年4月時点）</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件（目安）</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>3,500円</strong></td><td>本部レベル15到達</td><td>約583円/時</td></tr>
<tr><td>ポイントインカム</td><td>3,000円</td><td>本部レベル15到達</td><td>約500円/時</td></tr>
</table>
<p>※条件・報酬額は随時変動します。インストール直前に必ず案件ページで確認してください。</p>

<h2>ビビッドアーミーってどんなゲーム？</h2>
<p>ビビッドアーミーはポップでかわいらしいキャラクターが登場する城建設ストラテジーゲームです。グラフィックは明るくカジュアルですが、ゲームシステムはライキンやロードモバイルと同じです。「本部（城の中心建物）を指定レベルまで上げること」がポイ活の目標です。</p>
<p><strong>特徴：</strong>他の城ゲーと比べて建設時間が短め。3〜5日という短期間で達成しやすく、時給効率が高いAランク案件です。</p>

<h2>画面の基本構成</h2>
<ul>
<li><strong>本部（城の中心建物）</strong>：これを指定レベルにするのが目標</li>
<li><strong>ミッション（画面左のアイコン）</strong>：メインミッション。これに従って進めると資源・アイテムがもらえる</li>
<li><strong>スタミナ（画面右上）</strong>：モンスター討伐に使用。5分に1回復・最大100</li>
<li><strong>同盟（画面下）</strong>：加入すると建設ヘルプをもらえる</li>
</ul>

<h2>スタミナ管理</h2>
<ul>
<li><strong>最大値：</strong>100 / <strong>回復速度：</strong>5分に1回復（全回復約8時間20分）</li>
<li><strong>推奨サイクル：</strong>朝・昼・夜の3回プレイ</li>
<li><strong>使い道：</strong>マップのモンスター討伐 → 加速アイテム・資源入手</li>
</ul>

<h2>インストール直後にやること</h2>
<h3>ステップ1：チュートリアルを完了する</h3>
<p>指示に従うだけで本部はレベル4〜5程度になります。</p>

<h3>ステップ2：同盟に即加入する</h3>
<p>画面下の同盟アイコン → 「同盟を探す」→ 人数の多い同盟に申請。ヘルプで建設時間を大幅短縮できます。</p>

<h3>ステップ3：メインミッションを最優先で進める</h3>
<p>画面左のミッションアイコン → 上から順にクリア。大量の資源・加速アイテムがもらえます。</p>

<h2>建設の優先順位</h2>
<ol>
<li>農場・木材・鉱山・石材などの資源施設を全種類建設してレベルアップ</li>
<li>本部のアップグレード条件施設（本部タップ → 「条件」確認）を先にレベルアップ</li>
<li>本部を条件が揃ったらすぐアップグレード</li>
</ol>

<h2>日別攻略ロードマップ</h2>
<div class="day-roadmap">
<div class="day-roadmap__title">3〜5日間の完全攻略ステップ</div>
<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（約2時間）：チュートリアル完了・本部レベル6〜9</h4>
    <p>チュートリアル後すぐに同盟加入 → ミッションをこなす → スタミナでモンスター討伐 → 加速アイテムで建設短縮 → 就寝前に長時間建設をスタート。</p>
  </div>
</div>
<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2〜3（各1.5〜2時間）：本部レベル10〜13</h4>
    <p><strong>毎日のルーティン：</strong></p>
    <ol>
      <li>ミッション報酬を受け取る</li>
      <li>同盟ヘルプを送ってから要請する</li>
      <li>スタミナを全消化（モンスター討伐）</li>
      <li>採集部隊をマップに出す（資源ポイント → 採集 → 部隊派遣）</li>
      <li>建設完了したら即次の建設を開始</li>
    </ol>
  </div>
</div>
<div class="day-step day-step--final">
  <div class="day-step__num">4</div>
  <div class="day-step__content">
    <h4>Day 4〜5：本部レベル15達成 🎉</h4>
    <p>本部13〜15は資源が多く必要です。採集部隊を複数出しながら温存した加速アイテムを全投入。本部をタップして「レベル15」と表示されれば達成。ポイントサイトに1〜3週間で反映されます。</p>
  </div>
</div>
</div>

<h2>よくある質問 Q&A</h2>
<div class="faq-item"><div class="faq-item__q">本部のアップグレードができません</div><div class="faq-item__a">本部をタップ → 「条件」で不足施設を確認。赤表示の施設を先にレベルアップしてください。</div></div>
<div class="faq-item"><div class="faq-item__q">他の城ゲーと比べて何が違いますか？</div><div class="faq-item__a">建設時間が他の城ゲーより短く設定されているため、同じ日数でより高いレベルまで到達しやすいです。時給効率が高いのはそのためです。</div></div>
<div class="faq-item"><div class="faq-item__q">課金しないと無理ですか？</div><div class="faq-item__a">完全無課金で達成できます。ミッション報酬と同盟ヘルプで十分です。</div></div>
<div class="faq-item"><div class="faq-item__q">ポイントはいつ付きますか？</div><div class="faq-item__a">達成後1〜3週間でポイントサイトの管理画面に「未確定」として反映されます。</div></div>

<h2>まとめ：最短達成の4か条</h2>
<ol>
<li><strong>同盟に入ってヘルプを活用する</strong></li>
<li><strong>ミッションの指示通りに進める</strong></li>
<li><strong>スタミナを1日3回消化する</strong></li>
<li><strong>採集部隊を常に出しておく</strong></li>
</ol>
<div class="cta-box"><div class="cta-box__title">ゲームしながらポイントを貯めるなら「ポイカジ」も！</div><p class="cta-box__desc">30秒で遊べるカジュアルゲームで毎日コツコツ。複数のポイ活を掛け持ちするとさらにお得です。</p><a href="https://poicasi.co.jp" class="cta-box__btn" target="_blank" rel="noopener">ポイカジを始める →</a></div>"""

ARTICLE = {
    "title": "【ビビッドアーミー ポイ活攻略】5日で3,500円！時給583円の本部レベル達成法",
    "slug": "vivid-army-poikatsu-guide",
    "description": "ビビッドアーミーのポイ活攻略。本部レベル15到達を3〜5日・約6時間で達成してMoppyで3,500円を獲得する方法を操作レベルで解説。",
    "category": ["ゲーム攻略"],
    "articleType": ["game-guide"],
    "targetKeyword": "ビビッドアーミー ポイ活 攻略",
    "content": CONTENT
}

def post(data):
    allowed = {"title","slug","description","category","articleType","targetKeyword","content"}
    body = json.dumps({k:v for k,v in data.items() if k in allowed}, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(ENDPOINT, data=body,
        headers={"X-MICROCMS-API-KEY": API_KEY, "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req) as res:
        r = json.loads(res.read())
        print(f"[OK] ID={r.get('id')}")

if __name__ == "__main__":
    post(ARTICLE)
