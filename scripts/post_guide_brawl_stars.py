# -*- coding: utf-8 -*-
"""ブロスタ 詳細版投稿"""
import json, sys, urllib.request
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

CONTENT = """<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★★☆☆</span><span class="game-summary-item__label">難易度（少し腕前が必要）</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">5〜7日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約8時間</span><span class="game-summary-item__label">実質プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約375円/時</span><span class="game-summary-item__label">時給効率（Bランク）</span></div>
  </div>
</div>

<p><strong>この記事を読めばわかること：</strong>ブロスタを初めてプレイする方でも、5〜7日・約8時間でMoppyで最大3,000円を獲得できます。トロフィー数を指定数まで伸ばすための具体的な操作・バトル攻略・チケット（スタミナ）管理を解説します。</p>

<div class="warning-box"><strong>⚠️ 始める前に必ず確認</strong><p>ポイントサイトの案件ページを経由してからダウンロードしてください。達成条件（トロフィー数・特定ブロウラーの入手など）は案件によって異なります。インストール直前に必ず確認してください。</p></div>

<h2>ポイントサイト別 報酬比較（2026年4月時点）</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件（目安）</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>3,000円</strong></td><td>トロフィー500個到達</td><td>約375円/時</td></tr>
<tr><td>ポイントインカム</td><td>2,500円</td><td>トロフィー500個到達</td><td>約313円/時</td></tr>
</table>
<p>※条件・報酬額は随時変動します。インストール直前に必ず案件ページで確認してください。</p>

<h2>ブロスタってどんなゲーム？</h2>
<p>ブロスタは、個性豊かなキャラクター（ブロウラー）を使ってリアルタイムで3vs3バトルをするアクションゲームです。バトルに勝つとトロフィーが増えます。ポイ活の目標は「トロフィーを指定数（例：500）まで増やすこと」です。</p>
<p><strong>他のゲームとの違い：</strong>建設・放置系ではなく、アクションバトル系のゲームです。バトルに参加するスタミナ（チケット）が存在せず、バトルし放題です。その分プレイ時間が必要になります。</p>

<h2>画面の基本構成</h2>
<ul>
<li><strong>ホーム画面</strong>：所持ブロウラーの一覧・トロフィー数確認</li>
<li><strong>バトル（Play）ボタン</strong>：バトルモードを選んで対戦を始める</li>
<li><strong>ブロウラー</strong>：操作するキャラクター。最初は1〜2体からスタート。バトルで箱（ボックス）を集めると増える</li>
<li><strong>トロフィー（画面上部の金色のカップ）</strong>：バトル勝利で増える。これを指定数まで増やすのが目標</li>
<li><strong>ジェム（緑の宝石）</strong>：課金通貨。ポイ活では基本不使用でOK</li>
</ul>

<h2>バトルの基本操作</h2>
<p>バトル画面では左手で移動（左スティック）、右手で攻撃（右ボタン）を行います。</p>
<ul>
<li><strong>通常攻撃：</strong>右側の攻撃ボタンを敵の方向にスワイプして発射</li>
<li><strong>スーパー攻撃：</strong>攻撃を当てると黄色のゲージが溜まる → ゲージが満タンになると「スーパー攻撃」が使える → 大ダメージ</li>
<li><strong>基本戦術：</strong>草むら（緑の茂み）に隠れながら攻撃すると一方的に攻撃できる。草むらは最大の隠れ場所</li>
</ul>

<h2>おすすめバトルモードとトロフィーの稼ぎ方</h2>
<p><strong>「ジェムグラブ」がトロフィー効率最高：</strong>3vs3でジェムを10個集めてカウントダウンを耐えたチームの勝ちです。勝利でトロフィーが8〜10個増えます。</p>
<p><strong>操作手順：</strong>ホーム → 「Play（バトル）」ボタン → 「ジェムグラブ」を選択 → 「Play！」をタップ → マッチング後すぐバトル開始。</p>
<p><strong>負けてもトロフィーは減りにくい：</strong>負けた場合でも減るトロフィーは3〜4個程度です。勝てば8〜10増えるので、勝率50%以上あればトロフィーは増え続けます。</p>

<h2>最初に使うべきブロウラーの選び方</h2>
<p>最初にもらえるブロウラーの中から<strong>「シェリー（Shelly）」が初心者に最適</strong>です。</p>
<ul>
<li>体力が高く死にくい</li>
<li>散弾（ショットガン）で広範囲を攻撃できる</li>
<li>近距離で強いため草むら戦が得意</li>
</ul>
<p>ブロウラー選択：ホーム画面でブロウラーをタップ → 「選択」ボタンをタップ → バトルで使用するブロウラーが変更される。</p>

<h2>日別攻略ロードマップ</h2>
<div class="day-roadmap">
<div class="day-roadmap__title">5〜7日間の完全攻略ステップ</div>
<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（約1.5時間）：チュートリアル完了・トロフィー50〜100</h4>
    <p>チュートリアル後すぐにジェムグラブでバトル開始。1バトル約3〜4分。1時間で15〜20バトルできます。シェリーを使って草むらに隠れながら戦いましょう。</p>
    <p><strong>ボックス（宝箱）を必ず開ける：</strong>バトルをするとボックスが溜まります。ホーム画面右下のボックスアイコン → タップで開封。新しいブロウラーや強化アイテムが手に入ります。</p>
  </div>
</div>
<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2〜5（各1〜1.5時間）：トロフィー100〜400</h4>
    <p><strong>毎日のルーティン：</strong></p>
    <ol>
      <li>デイリーミッション確認（ホーム → イベント → デイリー）→ こなすとボックスや宝石がもらえる</li>
      <li>ジェムグラブを中心に1日10〜15バトル</li>
      <li>ボックスが溜まったら随時開封してブロウラーを強化</li>
    </ol>
    <p><strong>トロフィーが増えにくくなったら：</strong>ブロウラーを強化するかモードを変える（「バウンティ」「ハイスト」も試してみる）。自分のプレイスタイルに合ったモードを探しましょう。</p>
    <p><strong>トロフィーが高くなりすぎたブロウラーは使わない：</strong>トロフィーが高いと強い相手ばかりになります。まだ強化されていない別のブロウラーでバトルするほうがトロフィーを稼ぎやすいです。</p>
  </div>
</div>
<div class="day-step day-step--final">
  <div class="day-step__num">6</div>
  <div class="day-step__content">
    <h4>Day 6〜7：トロフィー500達成 🎉</h4>
    <p>合計トロフィーがホーム画面上部に表示されます。500に達したら達成です。ポイントサイトに1〜3週間で反映されます。</p>
  </div>
</div>
</div>

<h2>よくある質問 Q&A</h2>
<div class="faq-item"><div class="faq-item__q">バトルに全然勝てません</div><div class="faq-item__a">草むらに隠れながら攻撃することと、スーパー攻撃（黄色のゲージが満タンになったとき）を惜しまず使うことが基本です。また、ブロウラーのレベルを上げるとステータスが上がり勝ちやすくなります。</div></div>
<div class="faq-item"><div class="faq-item__q">スタミナがなくてバトルできません</div><div class="faq-item__a">ブロスタはスタミナ制ではありません。バトルし放題です。バトル回数に制限はないので、時間の許す限りプレイできます。</div></div>
<div class="faq-item"><div class="faq-item__q">課金しないと無理ですか？</div><div class="faq-item__a">トロフィー500程度は完全無課金で達成できます。バトルをこなせばボックスが貯まり、無料でブロウラーを強化できます。</div></div>
<div class="faq-item"><div class="faq-item__q">ポイントはいつ付きますか？</div><div class="faq-item__a">達成後1〜3週間でポイントサイトの管理画面に「未確定」として反映されます。</div></div>

<h2>まとめ：最短達成の3か条</h2>
<ol>
<li><strong>ジェムグラブを中心に1日10〜15バトルこなす</strong></li>
<li><strong>草むらに隠れながら攻撃する</strong>（生存率が上がり勝率が上がる）</li>
<li><strong>デイリーミッションをこなしてボックスを集める</strong>（ブロウラー強化で勝率アップ）</li>
</ol>
<div class="cta-box"><div class="cta-box__title">ゲームしながらポイントを貯めるなら「ポイカジ」も！</div><p class="cta-box__desc">30秒で遊べるカジュアルゲームで毎日コツコツ。複数のポイ活を掛け持ちするとさらにお得です。</p><a href="https://poicasi.co.jp" class="cta-box__btn" target="_blank" rel="noopener">ポイカジを始める →</a></div>"""

ARTICLE = {
    "title": "【ブロスタ ポイ活攻略】7日でトロフィー500！時給375円の効率バトル攻略",
    "slug": "brawl-stars-poikatsu-guide",
    "description": "ブロスタのポイ活攻略。トロフィー500到達を5〜7日・約8時間で達成してMoppyで3,000円を獲得する方法。バトルの基本操作・おすすめモード・ブロウラー選びを初心者向けに解説。",
    "category": ["ゲーム攻略"],
    "articleType": ["game-guide"],
    "targetKeyword": "ブロスタ ポイ活 攻略 トロフィー",
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
