# -*- coding: utf-8 -*-
"""ステートオブサバイバル 詳細版投稿"""
import json, sys, urllib.request
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

CONTENT = """<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★★☆☆</span><span class="game-summary-item__label">難易度（少し手間あり）</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">5〜7日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約9時間</span><span class="game-summary-item__label">実質プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約444円/時</span><span class="game-summary-item__label">時給効率（Aランク）</span></div>
  </div>
</div>

<p><strong>この記事を読めばわかること：</strong>ステートオブサバイバルを初めてインストールした方でも、5〜7日・約9時間でMoppyで最大4,000円を獲得できます。本拠地（HQ）を指定レベルにする方法を操作レベルで解説します。</p>

<div class="warning-box"><strong>⚠️ 始める前に必ず確認</strong><p>ポイントサイトの案件ページを経由してからダウンロードしてください。達成条件（HQレベル・生存者数など）は案件によって異なります。インストール直前に必ず確認してください。</p></div>

<h2>ポイントサイト別 報酬比較（2026年4月時点）</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件（目安）</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>4,000円</strong></td><td>本拠地HQ15到達</td><td>約444円/時</td></tr>
<tr><td>ポイントインカム</td><td>3,500円</td><td>本拠地HQ15到達</td><td>約389円/時</td></tr>
</table>
<p>※条件・報酬額は随時変動します。インストール直前に必ず案件ページで確認してください。</p>

<h2>ステートオブサバイバルってどんなゲーム？</h2>
<p>ゾンビウイルスが蔓延した世界で、生存者を集めて拠点（本拠地：HQ）を強化するサバイバルストラテジーゲームです。ポイ活の目標は「本拠地（HQ）を指定レベルまで上げること」。建設・資源収集・ゾンビ討伐を繰り返してHQレベルを上げていきます。</p>

<h2>画面の基本構成</h2>
<ul>
<li><strong>本拠地HQ（拠点中央の大きな建物）</strong>：これを指定レベルにするのが目標</li>
<li><strong>クエスト（画面左のアイコン）</strong>：メインクエスト。指示通りに進めると資源・加速アイテムがもらえる</li>
<li><strong>スタミナ（画面右上の炎マーク）</strong>：ゾンビ討伐に使用。6分に1回復・最大120</li>
<li><strong>同盟（画面下の旗マーク）</strong>：加入すると建設ヘルプをもらえる</li>
</ul>

<h2>スタミナ管理</h2>
<ul>
<li><strong>最大値：</strong>120 / <strong>回復速度：</strong>6分に1回復（全回復約12時間）</li>
<li><strong>推奨サイクル：</strong>朝・昼・夜の3回プレイでスタミナを使い切る</li>
<li><strong>使い道：</strong>ワールドマップのゾンビ討伐 → 資源・加速アイテム入手</li>
</ul>

<h2>インストール直後にやること</h2>
<h3>ステップ1：チュートリアルを完了する</h3>
<p>自動でチュートリアルが始まります。指示に従うだけでHQはレベル4〜5程度になります。</p>

<h3>ステップ2：同盟に入る（必須）</h3>
<p>画面下の旗マーク → 「同盟を探す」→ 人数の多い同盟に申請。<br>
<strong>理由：</strong>同盟に入ると「建設ヘルプ」が使えます。建設中の建物をタップ → 「ヘルプ要請」→ メンバーがタップするたびに建設時間が短縮されます。</p>

<h3>ステップ3：メインクエストを最優先で進める</h3>
<p>画面左のクエストアイコン → 「メインクエスト」→ 上から順にクリア。<strong>クエストの指示通りに進めるだけでOK。</strong>大量の資源・加速アイテムが手に入ります。</p>

<h2>建設の優先順位</h2>
<ol>
<li>農場・製材所・採石場・製鉄所（資源生産施設）を全種類建設してレベルを上げる</li>
<li>HQのアップグレード条件となる施設（HQをタップ → 「条件」で確認）を先にレベルアップ</li>
<li>HQを条件が揃ったらすぐアップグレード</li>
</ol>

<h2>日別攻略ロードマップ</h2>
<div class="day-roadmap">
<div class="day-roadmap__title">5〜7日間の完全攻略ステップ</div>
<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（約2時間）：チュートリアル完了・HQレベル6〜8</h4>
    <p>チュートリアル完了後すぐに同盟加入 → メインクエストをこなす → スタミナでゾンビ討伐 → 就寝前に長時間建設をスタート。</p>
  </div>
</div>
<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2〜5（各1.5〜2時間）：HQレベル9〜13</h4>
    <p><strong>毎日のルーティン：</strong></p>
    <ol>
      <li>クエスト報酬を受け取る</li>
      <li>同盟ヘルプを送る（同盟 → 「ヘルプ」→ メンバーの建設を支援）</li>
      <li>スタミナを全消化（マップでゾンビ討伐）</li>
      <li>採集部隊を出す（マップ → 資源ポイント → 「採集」→ 部隊派遣）</li>
      <li>建設完了したら即次の建設を開始</li>
    </ol>
  </div>
</div>
<div class="day-step day-step--final">
  <div class="day-step__num">6</div>
  <div class="day-step__content">
    <h4>Day 6〜7：HQ15達成 🎉</h4>
    <p>HQ13〜15のアップグレードには大量の資源が必要です。採集部隊を増やし、加速アイテムを全投入。HQをタップして「レベル15」と表示されれば達成。ポイントサイトに1〜3週間で反映されます。</p>
  </div>
</div>
</div>

<h2>よくある質問 Q&A</h2>
<div class="faq-item"><div class="faq-item__q">HQのアップグレードができません</div><div class="faq-item__a">HQをタップ → 「条件」で不足している施設レベルを確認。赤く表示された施設を先にレベルアップしてから再挑戦してください。</div></div>
<div class="faq-item"><div class="faq-item__q">資源が足りなくなります</div><div class="faq-item__a">採集部隊をマップに出し続けることが重要です。部隊が帰還したらすぐに再派遣しましょう。また、ゾンビ討伐で加速アイテムを集めて建設時間を短縮するのも有効です。</div></div>
<div class="faq-item"><div class="faq-item__q">課金しないと無理ですか？</div><div class="faq-item__a">完全無課金で達成できます。クエスト報酬と同盟ヘルプを活用すれば課金不要です。</div></div>
<div class="faq-item"><div class="faq-item__q">ポイントはいつ付きますか？</div><div class="faq-item__a">達成後1〜3週間でポイントサイトの管理画面に「未確定」として反映されます。</div></div>

<h2>まとめ：最短達成の4か条</h2>
<ol>
<li><strong>同盟に入ってヘルプを活用する</strong>（建設時間を大幅短縮）</li>
<li><strong>メインクエストの指示通りに進める</strong>（大量の資源・アイテム入手）</li>
<li><strong>スタミナを1日3回消化する</strong>（朝・昼・夜でゾンビ討伐）</li>
<li><strong>採集部隊を常に出しておく</strong>（放置で自動資源収集）</li>
</ol>
<div class="cta-box"><div class="cta-box__title">ゲームしながらポイントを貯めるなら「ポイカジ」も！</div><p class="cta-box__desc">30秒で遊べるカジュアルゲームで毎日コツコツ。複数のポイ活を掛け持ちするとさらにお得です。</p><a href="https://poicasi.co.jp" class="cta-box__btn" target="_blank" rel="noopener">ポイカジを始める →</a></div>"""

ARTICLE = {
    "title": "【ステートオブサバイバル ポイ活攻略】7日でHQ15達成！時給444円の最短手順",
    "slug": "state-of-survival-poikatsu-guide",
    "description": "ステートオブサバイバルのポイ活攻略。本拠地HQ15到達を5〜7日で達成してMoppyで4,000円を獲得する方法を操作レベルで解説。",
    "category": ["ゲーム攻略"],
    "articleType": ["game-guide"],
    "targetKeyword": "ステートオブサバイバル ポイ活 攻略",
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
