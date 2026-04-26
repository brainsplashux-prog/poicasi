# -*- coding: utf-8 -*-
"""コインマスター 詳細版投稿"""
import json, sys, urllib.request
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

ARTICLE = {
    "title": "【コインマスター ポイ活攻略】5日で3,500円！時給550円の村コンプ達成法",
    "slug": "coin-master-poikatsu-guide",
    "description": "コインマスターのポイ活攻略を完全解説。スピンの集め方・村の効率的な建設・デイリーリンクの活用まで初心者向けに操作レベルで解説。Moppyで3,500円・時給約550円のAランク案件。",
    "category": ["ゲーム攻略"],
    "articleType": ["game-guide"],
    "targetKeyword": "コインマスター ポイ活 攻略",
    "content": """
<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★☆☆☆</span><span class="game-summary-item__label">難易度（初心者OK）</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">3〜5日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約6〜7時間</span><span class="game-summary-item__label">実質プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約550円/時</span><span class="game-summary-item__label">時給効率（Aランク）</span></div>
  </div>
</div>

<p><strong>この記事を読めばわかること：</strong>コインマスターを初めてインストールした人でも、3〜5日・約6〜7時間で「村25コンプリート」などの達成条件をクリアし、Moppyで最大3,500円相当のポイントを獲得できます。スピンの集め方・村の建て方・デイリーリンクの場所まで操作レベルで解説します。</p>

<div class="warning-box"><strong>⚠️ 始める前に必ず確認</strong><p>Moppyなどのポイントサイトの案件ページを経由してからアプリをダウンロードしてください。達成条件（村のコンプリート数）は案件によって異なります。インストール前に必ず最新の条件を確認してください。</p></div>

<h2>ポイントサイト別 報酬比較（2026年4月時点）</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件（目安）</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>3,500円</strong></td><td>村25コンプリート</td><td>約550円/時</td></tr>
<tr><td>ポイントインカム</td><td>3,000円</td><td>村25コンプリート</td><td>約471円/時</td></tr>
<tr><td>ハピタス</td><td>2,800円</td><td>村25コンプリート</td><td>約440円/時</td></tr>
</table>
<p>※条件・報酬額は頻繁に変動します。必ずインストール直前に案件ページで確認してください。</p>

<h2>コインマスターってどんなゲーム？</h2>
<p>コインマスターは、スロットマシンを回して「コイン・アタック・レイド・盾・ジャックポット」の5種類の結果を出しながら、村を建設していくカジュアルゲームです。ポイ活の達成条件は「指定された村番号をコンプリート（すべての建物を建て終える）すること」です。</p>
<p>ゲームの核心は<strong>「スピン（スロットを回すこと）」</strong>。スピンを回してコインを集め、そのコインで村の建物を建てます。スピンは時間とともに自然回復しますが、デイリーリンクや友人招待などで追加入手できます。</p>

<h2>画面の基本構成（最初に覚える4つ）</h2>
<ul>
<li><strong>スロットマシン（画面中央）</strong>：スピンボタンを押してコインやアタック・レイドを獲得する</li>
<li><strong>村（画面上部の家アイコン）</strong>：コインを使って建物を建てる場所</li>
<li><strong>スピン残数（画面左下の数字）</strong>：残りスピン数。50回/時間で自然回復（最大50）</li>
<li><strong>コイン（画面上部の金色の数字）</strong>：村の建物を建てるための通貨</li>
</ul>

<h2>スピンの仕組みを理解する（最重要）</h2>
<ul>
<li><strong>スピン最大値：</strong>50（自然回復の上限）</li>
<li><strong>回復速度：</strong>1時間に50回（つまり約72分で50回満タン）</li>
<li><strong>注意：</strong>上限50を超えるとそれ以上は回復しない。スピンは溜め込まずこまめに使うこと</li>
<li><strong>デイリーリンクで毎日無料入手：</strong>1日あたり最大50〜100回分のスピンを無料でもらえる（後述）</li>
</ul>

<h2>インストール直後にやること</h2>

<h3>ステップ1：チュートリアルを終わらせる</h3>
<p>ゲームを開くと自動でチュートリアルが始まります。スピンの回し方・コインの使い方・村の建て方を学びながら最初の村がコンプリートされます。指示に従ってタップするだけでOKです。</p>

<h3>ステップ2：デイリーリンクを必ず毎日チェックする</h3>
<p>「コインマスター 無料スピンリンク 今日」でGoogle検索すると、当日限り有効の無料スピンリンクが見つかります。これをタップするだけで50〜100回分のスピンが無料でもらえます。<strong>毎日必ずやること</strong>です。</p>
<p>また、ゲーム内の「フレンドギフト」機能（画面下メニューの人型アイコン）でフェイスブック連携すると友人からスピンを受け取れます。フェイスブックアカウントがあれば連携しておきましょう。</p>

<h3>ステップ3：ペット「キツネ」を優先育成する</h3>
<p>ゲームを進めるとペット機能が解放されます（村レベルが上がると自動解放）。3種類のペットのうち<strong>「キツネ」を最優先で育てましょう。</strong>理由：キツネはレイド（他プレイヤーの村から掘ってコインを奪う）のときにボーナスコインが増えるため、コイン収集効率が大幅に上がります。</p>
<p>ペット画面の開き方：画面下メニューの「ペット」アイコン（足跡マーク）をタップ → キツネを選んで「育成」。</p>

<h2>日別攻略ロードマップ</h2>

<div class="day-roadmap">
<div class="day-roadmap__title">3〜5日間の完全攻略ステップ</div>

<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（プレイ時間：約1.5時間）：村1〜8をコンプリート</h4>
    <p><strong>◆ 毎日最初にやること（2〜3分）</strong></p>
    <ol>
      <li>「コインマスター 無料スピンリンク 今日」でGoogle検索 → 最新リンクをタップ → スピン受け取り</li>
      <li>ゲーム内のフレンドギフトを確認（もらえるスピンがあれば受け取る）</li>
      <li>ペットのエサをあげる（ペット → 「エサをあげる」でペットの効果が一定時間継続）</li>
    </ol>
    <p><strong>◆ スピンを回してコインを集める</strong><br>
    画面中央の大きなスピンボタンをタップ。「コイン3つ」が揃うと大量のコインが入ります。「豚マーク（レイド）」が出たら他プレイヤーの村を掘ってコインを奪います（画面の指示に従う）。</p>
    <p><strong>◆ コインで村の建物を建てる</strong><br>
    画面上部の「村」アイコンをタップ → 村の画面に移動 → 建物アイコンをタップして建設。建物は5つあり、全部建設＋アップグレードが完了すると「村コンプリート」です。次の村に進めます。</p>
    <p><strong>◆ 盾を貯めておく</strong><br>
    スロットで「盾マーク」が出ると、他プレイヤーからのアタック（村が壊される）を1回防げます。盾は最大3枚まで保持できます。村を建てている最中は必ず盾を3枚持つようにしましょう。</p>
  </div>
</div>

<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2〜3（各1.5〜2時間）：村9〜20をコンプリート</h4>
    <p><strong>◆ コインが足りなくなったらスピンで補充</strong><br>
    村が進むにつれて建設に必要なコインが増えます。スピンが足りない場合はデイリーリンクで補充。イベント（画面右上のイベントアイコン）が開催中なら積極的に参加するとスピンが大量にもらえます。</p>
    <p><strong>◆ レイドのコツ</strong><br>
    レイド画面（豚マークが出たとき）では、掘る場所を3つ選べます。ランダムですが、「キツネのペット効果がある状態」で行うとボーナスコインが入ります。ペットのエサは残り時間を確認してから使いましょう。</p>
    <p><strong>◆ 村が壊されたら？</strong><br>
    他プレイヤーのアタックで建物が壊されることがあります。壊された建物は「修復」ボタンをタップして再建設するだけです（コインが必要）。焦らず修復して進めましょう。</p>
    <p><strong>◆ ベット数を調整してコインを一気に稼ぐ</strong><br>
    スピン画面左下に「ベット数（×1〜×10）」があります。コインが十分あるときに「×3〜×5」に上げてスピンすると1回で獲得できるコインが増え、効率的に村を建設できます。</p>
  </div>
</div>

<div class="day-step day-step--final">
  <div class="day-step__num">4</div>
  <div class="day-step__content">
    <h4>Day 4〜5：村25コンプリートで達成 🎉</h4>
    <p><strong>◆ 達成直前の注意</strong><br>
    村25の最後の建物を建設する前に、盾を3枚持っているか確認しましょう。アタックで壊されると達成が遅れます。</p>
    <p><strong>◆ 達成確認の方法</strong><br>
    村25の全建物が完成すると「村コンプリート！」の演出が出ます。ポイントサイトの管理画面で「未確定ポイント」として記録されます。反映まで1〜3週間かかります。</p>
  </div>
</div>
</div>

<h2>よくある質問 Q&A</h2>
<div class="faq-item"><div class="faq-item__q">スピンが全然足りません</div><div class="faq-item__a">毎日の「無料スピンリンク」が最重要です。Google で「コインマスター 無料スピンリンク 今日」と検索して当日のリンクをタップするだけで最大100回分が無料でもらえます。また、ゲーム内イベントに参加するとまとめてスピンがもらえます。</div></div>
<div class="faq-item"><div class="faq-item__q">村が何度もアタックされて壊れます</div><div class="faq-item__a">盾を3枚キープするのが基本です。スロットで盾が出たら大切に使いましょう。また、コインを大量に持ったまま放置するとレイドで大量に奪われます。コインが溜まったらすぐに村の建設に使いましょう。</div></div>
<div class="faq-item"><div class="faq-item__q">課金しないと進めませんか？</div><div class="faq-item__a">村25程度は完全無課金で達成できます。デイリーリンクとイベントを活用すれば、課金なしで十分なスピンが確保できます。</div></div>
<div class="faq-item"><div class="faq-item__q">ポイントはいつ付きますか？</div><div class="faq-item__a">達成後、ポイントサイトの管理画面に「未確定」として表示されます。「確定」になるまで通常1〜3週間かかります。表示されない場合はポイントサイトのサポートに達成時刻とスクリーンショットを添えて問い合わせてください。</div></div>
<div class="faq-item"><div class="faq-item__q">フェイスブック連携は必須ですか？</div><div class="faq-item__a">必須ではありません。ただし連携するとフレンドからのスピンギフト受け取りや、ゲームデータのバックアップができるためおすすめです。</div></div>

<h2>まとめ：最短達成の3か条</h2>
<ol>
<li><strong>毎日デイリーリンクでスピンを無料補充する</strong>（最大100回/日）</li>
<li><strong>コインが溜まったらすぐ村の建設に使う</strong>（レイドで奪われる前に）</li>
<li><strong>スピン上限50を溢れさせない</strong>（1〜2時間おきにゲームを開く）</li>
</ol>
<p>コインマスターは運要素も高いですが、デイリーリンクを毎日活用すれば3〜5日で無課金達成できます。Moppyで最大3,500円を狙いましょう。</p>
<div class="cta-box"><div class="cta-box__title">ゲームしながらポイントを貯めるなら「ポイカジ」も！</div><p class="cta-box__desc">30秒で遊べるカジュアルゲームで毎日コツコツ。複数のポイ活を掛け持ちするとさらにお得です。</p><a href="https://poicasi.co.jp" class="cta-box__btn" target="_blank" rel="noopener">ポイカジを始める →</a></div>
"""
}

def post(data):
    allowed = {"title","slug","description","category","articleType","targetKeyword","content"}
    body = json.dumps({k:v for k,v in data.items() if k in allowed}, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(ENDPOINT, data=body,
        headers={"X-MICROCMS-API-KEY": API_KEY, "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req) as res:
        r = json.loads(res.read())
        print(f"[OK] ID={r.get('id')} : {data['title'][:50]}")

if __name__ == "__main__":
    post(ARTICLE)
