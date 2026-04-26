# -*- coding: utf-8 -*-
import json, sys, urllib.request
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

CONTENT = """<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★★☆☆</span><span class="game-summary-item__label">難易度（パズルが少し難しい）</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">5〜7日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約7〜8時間</span><span class="game-summary-item__label">実質プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約375円/時</span><span class="game-summary-item__label">時給効率（Bランク）</span></div>
  </div>
</div>

<p><strong>この記事を読めばわかること：</strong>ホームスケイプを一度もプレイしたことがない方でも、5〜7日・約7〜8時間でMoppyで最大3,000円を獲得できます。マッチ3パズルをクリアして部屋を改装していく攻略手順を操作レベルで解説します。</p>

<div class="warning-box"><strong>⚠️ 始める前に必ず確認</strong><p>ポイントサイトの案件ページを経由してからダウンロードしてください。達成条件（エリア・部屋の改装数など）は案件によって異なります。インストール直前に必ず確認してください。</p></div>

<h2>ポイントサイト別 報酬比較（2026年4月時点）</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件（目安）</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>3,000円</strong></td><td>部屋改装5〜6室完了</td><td>約375円/時</td></tr>
<tr><td>ポイントインカム</td><td>2,500円</td><td>部屋改装5〜6室完了</td><td>約313円/時</td></tr>
</table>
<p>※条件・報酬額は随時変動します。インストール直前に必ず案件ページで確認してください。</p>

<h2>ホームスケイプってどんなゲーム？</h2>
<p>ホームスケイプはマッチ3パズル（同じ色のタイルを3つ以上並べて消す）をクリアして星（スター）を集め、オースティンという執事キャラクターの家（邸宅）を部屋ごとに改装していくゲームです。ガーデンスケイプと同じ開発会社のゲームで、システムはほぼ同じです。</p>
<p>ポイ活の目標は「指定の部屋数を改装すること」。パズルをクリアするたびに星が1つもらえ、星を使って部屋の家具・内装を選んで改装します。</p>

<h2>画面の基本構成</h2>
<ul>
<li><strong>邸宅（メイン画面）</strong>：改装する部屋を選ぶ。改装したい箇所をタップ → 必要な星数が表示される → 「改装」</li>
<li><strong>パズル画面</strong>：「プレイ」ボタンで開始。クリアすると星が1つもらえる</li>
<li><strong>ライフ（ハートマーク・画面上部左）</strong>：パズルをプレイするたびに1消費。最大5つ・30分に1回復</li>
<li><strong>コイン（画面上部右）</strong>：パズル中の手数追加や緊急ブースターに使用。温存推奨</li>
</ul>

<h2>ライフ（スタミナ）管理</h2>
<ul>
<li><strong>最大値：</strong>5 / <strong>回復速度：</strong>30分に1回復（全回復2時間30分）</li>
<li><strong>推奨サイクル：</strong>2〜3時間おきにゲームを開いてライフを使い切る（1日4〜5回）</li>
<li><strong>コツ：</strong>ライフが溢れると回復が止まるため、こまめにプレイすること</li>
</ul>

<h2>インストール直後にやること</h2>
<h3>ステップ1：チュートリアルを完了する</h3>
<p>オースティンが案内してくれます。指示に従うだけで最初の部屋改装が完了します。</p>

<h3>ステップ2：コインを「手数追加」以外に使わない</h3>
<p>コインはパズル中に「手数追加（+5手・900コイン）」ボタンが出ます。<strong>序盤（部屋1〜3）では絶対に使わない。</strong>後半の難しいパズルのために温存しましょう。</p>

<h3>ステップ3：改装する箇所は「星が少ない項目」を選ぶ</h3>
<p>改装箇所をタップすると必要な星数が表示されます。星1〜2個で改装できる箇所を優先して進めましょう。</p>

<h2>パズル攻略のコツ</h2>
<ul>
<li><strong>下から消す：</strong>下部のタイルを消すと連鎖が起きやすくなる</li>
<li><strong>爆弾（4つ一直線）・ロケット（L字5つ）・レインボーボール（同色5つ以上直線）</strong>を作って障害物を一気に消す</li>
<li><strong>レインボーボールは温存：</strong>障害物が多いステージや残り手数が少ないときに使う</li>
</ul>

<h2>日別攻略ロードマップ</h2>
<div class="day-roadmap">
<div class="day-roadmap__title">5〜7日間の完全攻略ステップ</div>
<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（約1.5時間）：チュートリアル完了・部屋1〜2改装</h4>
    <p>チュートリアル後すぐにパズルを開始。5ライフ（5回）使い切ったら2〜3時間待って再プレイ。1日に4〜5セット（20〜25回パズル）をこなすことを目標にします。</p>
  </div>
</div>
<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2〜5（各1〜1.5時間）：部屋3〜5改装</h4>
    <p><strong>毎日のルーティン：</strong></p>
    <ol>
      <li>朝起きたら5ライフ分パズルをプレイ（約15〜20分）</li>
      <li>2〜3時間後にまた5ライフ分プレイ</li>
      <li>昼・夕方・夜と繰り返す（1日4〜5セット）</li>
      <li>集めた星で部屋の改装を進める</li>
    </ol>
    <p><strong>難しいパズルで詰まったら：</strong>同じステージを何度もリトライしても焦らない。下部から消すことと特殊タイルを作ることを意識しましょう。</p>
  </div>
</div>
<div class="day-step day-step--final">
  <div class="day-step__num">6</div>
  <div class="day-step__content">
    <h4>Day 6〜7：指定部屋数の改装完了 🎉</h4>
    <p>後半の部屋（5〜6室目）は難しいパズルが増えます。ここでコインを使って手数追加をしても構いません。改装完了後、ポイントサイトに1〜3週間で反映されます。</p>
  </div>
</div>
</div>

<h2>よくある質問 Q&A</h2>
<div class="faq-item"><div class="faq-item__q">ガーデンスケイプとどう違いますか？</div><div class="faq-item__a">ゲームシステムはほぼ同じです。ガーデンスケイプは「庭を修復」、ホームスケイプは「家を改装」というテーマの違いです。どちらか一方をクリアした経験があればすぐに慣れます。</div></div>
<div class="faq-item"><div class="faq-item__q">ライフが回復するのが遅い</div><div class="faq-item__a">30分に1回復なので、2〜3時間おきにプレイするのが最効率です。Facebookと連携すると友人からライフを送ってもらえる場合があります。</div></div>
<div class="faq-item"><div class="faq-item__q">課金しないと無理ですか？</div><div class="faq-item__a">完全無課金で達成できます。コインを後半に温存し、ブースターをデイリー報酬でコツコツ集めれば十分です。</div></div>
<div class="faq-item"><div class="faq-item__q">ポイントはいつ付きますか？</div><div class="faq-item__a">達成後1〜3週間でポイントサイトに「未確定」として反映されます。</div></div>

<h2>まとめ：最短達成の3か条</h2>
<ol>
<li><strong>ライフを2〜3時間おきに使い切る</strong></li>
<li><strong>コインは後半の難しいパズルのために温存する</strong></li>
<li><strong>下部タイルから消して特殊タイルを作る</strong></li>
</ol>
<div class="cta-box"><div class="cta-box__title">ゲームしながらポイントを貯めるなら「ポイカジ」も！</div><p class="cta-box__desc">30秒で遊べるカジュアルゲームで毎日コツコツ。複数のポイ活を掛け持ちするとさらにお得です。</p><a href="https://poicasi.co.jp" class="cta-box__btn" target="_blank" rel="noopener">ポイカジを始める →</a></div>"""

ARTICLE = {
    "title": "【ホームスケイプ ポイ活攻略】7日で3,000円！部屋改装の最短達成手順",
    "slug": "homescapes-poikatsu-guide",
    "description": "ホームスケイプのポイ活攻略。部屋改装条件を5〜7日・約7〜8時間で達成してMoppyで3,000円を獲得する方法。パズル攻略・ライフ管理を初心者向けに操作レベルで解説。",
    "category": ["ゲーム攻略"],
    "articleType": ["game-guide"],
    "targetKeyword": "ホームスケイプ ポイ活 攻略",
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
