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
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★☆☆☆</span><span class="game-summary-item__label">難易度（初心者OK）</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">3〜5日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約6時間</span><span class="game-summary-item__label">実質プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約583円/時</span><span class="game-summary-item__label">時給効率（Aランク）</span></div>
  </div>
</div>

<p><strong>この記事を読めばわかること：</strong>エバーテイルを初めてプレイする方でも、3〜5日・約6時間でMoppyで最大3,500円を獲得できます。チャプター進行・スタミナ管理・モンスター強化の具体的な操作手順を解説します。</p>

<div class="warning-box"><strong>⚠️ 始める前に必ず確認</strong><p>ポイントサイトの案件ページを経由してからダウンロードしてください。達成条件（チャプター数・プレイヤーレベルなど）は案件によって異なります。インストール直前に必ず確認してください。</p></div>

<h2>ポイントサイト別 報酬比較（2026年4月時点）</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件（目安）</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>3,500円</strong></td><td>チャプター3〜4クリア</td><td>約583円/時</td></tr>
<tr><td>ポイントインカム</td><td>3,000円</td><td>チャプター3〜4クリア</td><td>約500円/時</td></tr>
</table>
<p>※条件・報酬額は随時変動します。インストール直前に必ず案件ページで確認してください。</p>

<h2>エバーテイルってどんなゲーム？</h2>
<p>エバーテイルはポケモンに似たモンスター収集RPGです。フィールドを探索しながらモンスターを捕まえ、育てて戦わせます。ポイ活の目標は「指定チャプター（例：チャプター4）をクリアすること」。ストーリーを進めながらバトルをこなしていきます。</p>
<p><strong>特徴：</strong>スタミナが回復するまでの待ち時間が比較的短く、1日あたりのプレイ量が多いため短期間で達成しやすいゲームです。</p>

<h2>画面の基本構成</h2>
<ul>
<li><strong>ワールドマップ</strong>：チャプターを選んでストーリーを進める</li>
<li><strong>バトル画面</strong>：ターン制コマンドバトル。「攻撃」「スキル」「アイテム」「逃げる」から選択</li>
<li><strong>スタミナ（画面右上の炎マーク）</strong>：バトル・探索に使用。4分に1回復・最大60</li>
<li><strong>モンスターボックス（画面下）</strong>：所持モンスターの管理・強化</li>
</ul>

<h2>スタミナ管理</h2>
<ul>
<li><strong>最大値：</strong>60 / <strong>回復速度：</strong>4分に1回復（全回復約4時間）</li>
<li><strong>推奨サイクル：</strong>4〜5時間おきにゲームを開いてスタミナを消化（1日3〜4回）</li>
<li><strong>ポイント：</strong>全回復が早いため、こまめにプレイすると1日のプレイ量が多くなる</li>
</ul>

<h2>インストール直後にやること</h2>
<h3>ステップ1：チュートリアルを完了する</h3>
<p>ストーリーが流れます。バトルの基本操作が自動で教えられます。チュートリアル後にチャプター1の序盤が完了します。</p>

<h3>ステップ2：最初のモンスターを決める</h3>
<p>ゲーム開始時に3体の初期モンスターから1体を選びます。<strong>どれを選んでもチャプター4クリアには影響しません。</strong>見た目の好みで選んでOKです。</p>

<h3>ステップ3：バトルはオートモードを使う</h3>
<p>バトル画面右上に「オートバトル」ボタンがあります。タップするとモンスターが自動で攻撃します。チャプター序盤はオートで問題なくクリアできます。</p>

<h2>チャプター攻略のコツ</h2>
<ul>
<li><strong>チャプターを順番に進める：</strong>ワールドマップ → チャプター番号を順にタップ → 「バトル開始」。ストーリーが流れたら「スキップ」でOK</li>
<li><strong>モンスターが弱くなったら強化：</strong>画面下の「モンスター」アイコン → 強化したいモンスターをタップ → 「レベルアップ」→ 経験値素材を使う</li>
<li><strong>負けたら属性相性を確認：</strong>水・炎・草・電気などの属性相性があります。弱点属性のモンスターで攻撃すると大ダメージ。バトル画面で敵の属性アイコンを確認して有利な属性で攻めましょう</li>
</ul>

<h2>日別攻略ロードマップ</h2>
<div class="day-roadmap">
<div class="day-roadmap__title">3〜5日間の完全攻略ステップ</div>
<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（約2時間）：チュートリアル完了・チャプター1クリア</h4>
    <p>チュートリアル後すぐにオートバトルで進める。チャプター1の全バトルをクリアしたら次へ。スタミナが切れたら4時間待つか、回復アイテムを使う。就寝前にスタミナを使い切る。</p>
  </div>
</div>
<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2〜3（各1.5〜2時間）：チャプター2〜3クリア</h4>
    <p><strong>毎日のルーティン：</strong></p>
    <ol>
      <li>朝起きたらスタミナが全回復している → 即バトル開始</li>
      <li>スタミナ切れ → 4時間待つ間に他のことをする</li>
      <li>夕方・夜にまたプレイ（1日3〜4回）</li>
      <li>デイリーミッション（画面左のアイコン）を確認して達成分の報酬を受け取る</li>
    </ol>
    <p><strong>バトルで詰まったら：</strong>モンスターをレベルアップ（モンスター画面 → レベルアップ）か、属性有利なモンスターに変えて再挑戦。</p>
  </div>
</div>
<div class="day-step day-step--final">
  <div class="day-step__num">4</div>
  <div class="day-step__content">
    <h4>Day 4〜5：チャプター4クリアで達成 🎉</h4>
    <p>チャプター4のラストバトルをクリアすれば条件達成です。ポイントサイトに1〜3週間で反映されます。</p>
  </div>
</div>
</div>

<h2>よくある質問 Q&A</h2>
<div class="faq-item"><div class="faq-item__q">バトルに負けて進めません</div><div class="faq-item__a">モンスターのレベルが低い可能性があります。モンスター画面でレベルアップ用の経験値素材を使ってレベルを上げましょう。また、属性相性も確認してください（水は炎に強い・炎は草に強いなど）。</div></div>
<div class="faq-item"><div class="faq-item__q">モンスターの捕まえ方がわかりません</div><div class="faq-item__a">バトル中に敵のHPを赤ゾーンまで減らしてから「捕まえる」コマンドを選択します。捕まえられる確率が上がります。ただし、チャプタークリアが目的なら積極的に捕まえなくてもOKです。</div></div>
<div class="faq-item"><div class="faq-item__q">課金しないと無理ですか？</div><div class="faq-item__a">チャプター4程度は完全無課金で達成できます。デイリー報酬とバトルで手に入る素材で十分です。</div></div>
<div class="faq-item"><div class="faq-item__q">ポイントはいつ付きますか？</div><div class="faq-item__a">達成後1〜3週間でポイントサイトに「未確定」として反映されます。</div></div>

<h2>まとめ：最短達成の3か条</h2>
<ol>
<li><strong>スタミナを4〜5時間おきに使い切る</strong>（全回復が早いので1日3〜4回プレイ可能）</li>
<li><strong>オートバトルを活用してサクサク進める</strong></li>
<li><strong>バトルで詰まったらモンスターのレベルアップと属性確認</strong></li>
</ol>
<div class="cta-box"><div class="cta-box__title">ゲームしながらポイントを貯めるなら「ポイカジ」も！</div><p class="cta-box__desc">30秒で遊べるカジュアルゲームで毎日コツコツ。複数のポイ活を掛け持ちするとさらにお得です。</p><a href="https://poicasi.co.jp" class="cta-box__btn" target="_blank" rel="noopener">ポイカジを始める →</a></div>"""

ARTICLE = {
    "title": "【エバーテイル ポイ活攻略】5日で3,500円！時給583円のチャプター達成法",
    "slug": "evertale-poikatsu-guide",
    "description": "エバーテイルのポイ活攻略。チャプター4クリアを3〜5日・約6時間で達成してMoppyで3,500円を獲得する方法。オートバトル・スタミナ管理・モンスター強化を初心者向けに解説。",
    "category": ["ゲーム攻略"],
    "articleType": ["game-guide"],
    "targetKeyword": "エバーテイル ポイ活 攻略 チャプター",
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
