# -*- coding: utf-8 -*-
"""クラッシュオブクラン 詳細版投稿"""
import json, sys, urllib.request
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

ARTICLE = {
    "title": "【クラッシュオブクラン ポイ活攻略】7日でTH7達成！時給450円の効率攻略",
    "slug": "clash-of-clans-poikatsu-guide",
    "description": "クラッシュオブクランのポイ活攻略を完全解説。タウンホール7（TH7）到達を7日・約10時間で達成する具体的な手順。資源の略奪方法・建設優先順位・ジェムの使い道まで初心者向けに操作レベルで解説。",
    "category": ["ゲーム攻略"],
    "articleType": ["game-guide"],
    "targetKeyword": "クラッシュオブクラン ポイ活 攻略 TH7",
    "content": """
<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★★☆☆</span><span class="game-summary-item__label">難易度（少し手間あり）</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">5〜7日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約10時間</span><span class="game-summary-item__label">実質プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約450円/時</span><span class="game-summary-item__label">時給効率（Aランク）</span></div>
  </div>
</div>

<p><strong>この記事を読めばわかること：</strong>クラッシュオブクラン（クラクラ）を初めてプレイする方でも、5〜7日・約10時間でタウンホール7（TH7）に到達してMoppyで最大4,500円を獲得する方法を、操作手順レベルで解説します。資源の効率的な集め方・建設の優先順位・「略奪」の具体的なやり方まで網羅します。</p>

<div class="warning-box"><strong>⚠️ 始める前に必ず確認</strong><p>ポイントサイトの案件ページを経由してからダウンロードしてください。案件によってはTH7ではなく別の条件（村人数・施設レベルなど）が指定されている場合があります。インストール前に必ず達成条件を確認してください。</p></div>

<h2>ポイントサイト別 報酬比較（2026年4月時点）</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件（目安）</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>4,500円</strong></td><td>タウンホール7到達</td><td>約450円/時</td></tr>
<tr><td>ポイントインカム</td><td>4,000円</td><td>タウンホール7到達</td><td>約400円/時</td></tr>
<tr><td>ハピタス</td><td>3,500円</td><td>タウンホール7到達</td><td>約350円/時</td></tr>
</table>
<p>※条件・報酬額は随時変動します。インストール直前に必ず案件ページで確認してください。</p>

<h2>クラッシュオブクランってどんなゲーム？</h2>
<p>クラッシュオブクラン（クラクラ）は、自分の村を強化しながら他プレイヤーの村を攻撃して資源を奪い合うストラテジーゲームです。ポイ活の達成条件は「タウンホール（村の中心施設）をレベル7にすること」。タウンホールのレベルアップには大量の資源（ゴールド・エリクサー）が必要で、これを集めるために他プレイヤーの村を「略奪（マルチプレイ攻撃）」するのが最も効率的な方法です。</p>

<h2>画面の基本構成（最初に覚える5つ）</h2>
<ul>
<li><strong>タウンホール（村の中心の大きな建物）</strong>：これをレベル7にするのが目標</li>
<li><strong>ゴールド貯蔵庫（金のドーム型）</strong>：ゴールドを貯める倉庫。タウンホールのアップに必要</li>
<li><strong>エリクサー貯蔵庫（紫の丸い建物）</strong>：エリクサーを貯める倉庫。兵士の訓練・呪文に必要</li>
<li><strong>兵舎（兵士マーク）</strong>：攻撃用の兵士を訓練する場所</li>
<li><strong>ビルダー（小人のキャラクター）</strong>：建物を建設・アップグレードする職人。同時建設できる数はビルダーの数に依存（最初は2人）</li>
</ul>

<h2>資源（ゴールド・エリクサー）の集め方</h2>
<p>タウンホールを上げるには大量のゴールドが必要です。最も効率的な方法は<strong>「マルチプレイで他プレイヤーの村を攻撃して略奪すること」</strong>です。</p>
<p><strong>略奪の手順：</strong><br>
画面下メニューの「攻撃」（剣マーク）をタップ → 「マルチプレイヤーを攻撃」→ 「次を探す」で相手を探す → 資源が多くて守りが弱い村が見つかったら「攻撃！」をタップ → 兵士を配置して略奪。</p>
<p><strong>効率的な相手の選び方：</strong>「次を探す」で複数の村を見比べて、ゴールド/エリクサーが100万以上溜まっていてタウンホールが低い（TH4〜5）村を狙いましょう。そういった村は防衛が弱く略奪しやすいです。</p>

<h2>インストール直後にやること（超重要）</h2>

<h3>ステップ1：チュートリアルを完了する</h3>
<p>最初に「バーバリアンキング」というキャラクターが操作方法を教えてくれます。指示に従ってタップするだけで基本操作が覚えられます。チュートリアル後にタウンホールはLv3程度になっています。</p>

<h3>ステップ2：ジェム（課金通貨）はビルダー追加のみに使う</h3>
<p>最初にジェム（緑の宝石）が500個程度もらえます。<strong>このジェムは「ビルダーを追加（3人目）」に使いましょう。</strong><br>
操作：村の画面 → 「+ビルダー」アイコンをタップ → 250ジェムで3人目のビルダーを雇用。これにより同時に3つの建設が可能になり、建設効率が大幅に上がります。残りのジェムは急ぎの建設短縮に使います。</p>

<h3>ステップ3：シールドを有効活用する</h3>
<p>最初の数日間は「シールド（他プレイヤーから攻撃されない保護）」が有効です。シールド中は安全に建設を進められます。シールドが切れたら自分も攻撃されるリスクが出ますが、タウンホールを守るより略奪を優先する戦略で進めましょう。</p>

<h2>TH7までの建設優先順位</h2>
<p>タウンホールをレベルアップするには「条件となる施設のアップグレード」は不要です。ゴールドさえ集めれば直接TH7にアップできます。以下の優先順位で進めましょう。</p>
<ol>
<li><strong>ゴールド採掘機・ゴールド貯蔵庫</strong>を先にアップ（自動でゴールドが増える）</li>
<li><strong>兵舎</strong>をアップして強い兵士（ジャイアント・アーチャー）を訓練できるようにする</li>
<li><strong>タウンホール</strong>を直接アップグレード（TH4→5→6→7と順番に）</li>
</ol>
<p>防衛施設（大砲・アーチャータワーなど）は後回しでOKです。ポイ活には防衛力より攻撃・資源収集が重要です。</p>

<h2>日別攻略ロードマップ</h2>

<div class="day-roadmap">
<div class="day-roadmap__title">5〜7日間の完全攻略ステップ</div>

<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（プレイ時間：約2時間）：チュートリアル完了・TH4〜5</h4>
    <p><strong>◆ チュートリアル完了後すぐにマルチ攻撃を開始する</strong><br>
    資源が少ない場合、待たずにマルチプレイで略奪します。兵士（バーバリアン）を訓練 → 攻撃ボタン → マルチプレイヤーを攻撃 → 「次を探す」で資源の多い相手を探す → 攻撃。</p>
    <p><strong>◆ 「クランに入る」は後回しでOK</strong><br>
    TH5になるとクラン機能が解放されます。クランに入ることで支援兵士をもらえますが、序盤はまず自力で進めましょう。</p>
    <p><strong>◆ 寝る前に長時間かかる建設をスタートする</strong><br>
    TH4〜5のアップグレードには数時間〜1日かかります。就寝前にスタートして翌朝完成させましょう。</p>
  </div>
</div>

<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2〜4（各1.5〜2時間）：TH5〜6</h4>
    <p><strong>◆ 毎日の略奪ルーティン</strong></p>
    <ol>
      <li>兵士の訓練が完了しているか確認（兵舎をタップ → 残り時間確認）</li>
      <li>マルチプレイ攻撃 → 3〜5回略奪してゴールドを集める</li>
      <li>集めたゴールドをすぐに建設・アップグレードに使う（貯め込まない）</li>
    </ol>
    <p><strong>◆ 略奪後はすぐ建設する（貯め込みNG）</strong><br>
    ゴールドを大量に持っていると、自分が攻撃されたときに略奪されます。略奪したらすぐにタウンホールやゴールド採掘機のアップグレードに使いましょう。</p>
    <p><strong>◆ TH6到達のタイミングでクランに入る</strong><br>
    画面下の「クラン」アイコン → 「クランを探す」→ 人数が多くアクティブなクランを選んで申請。クランに入ると支援兵士（強い兵士を借りられる）をもらえるため、攻撃力が一気に上がります。</p>
  </div>
</div>

<div class="day-step day-step--final">
  <div class="day-step__num">6</div>
  <div class="day-step__content">
    <h4>Day 5〜7：TH7達成 🎉</h4>
    <p><strong>◆ TH7アップグレードに必要なゴールドを一気に集める</strong><br>
    TH7のアップグレードには約125万ゴールドが必要です。マルチ略奪を1日3〜5回行い、ゴールドが集まったらすぐにアップグレードをタップ。</p>
    <p><strong>◆ アップグレード中も別の建設を進める</strong><br>
    TH7のアップグレードには数日かかります（ジェムで短縮可）。その間も他の施設（ゴールド採掘機など）のアップをビルダーに並行でやらせましょう。</p>
    <p><strong>◆ 達成確認の方法</strong><br>
    タウンホールをタップして「レベル7」と表示されていればOK。ポイントサイトに反映まで1〜3週間かかります。</p>
  </div>
</div>
</div>

<h2>よくある質問 Q&A</h2>
<div class="faq-item"><div class="faq-item__q">攻撃してもすぐ負けてしまいます</div><div class="faq-item__a">兵士の種類と配置が重要です。ジャイアント（体力が高い）を前に出して敵の防衛施設を引き付け、後ろからアーチャーやゴブリンで攻撃するのが基本です。また、敵のタウンホールが置いてある隅を狙うと効率よくゴールドを奪えます。</div></div>
<div class="faq-item"><div class="faq-item__q">建設に何日もかかると表示されます</div><div class="faq-item__a">高いレベルの施設ほど時間がかかります。ジェムで短縮するか、就寝前・外出前にスタートして待ちましょう。TH7のアップグレードは3〜4日かかるため、早めにゴールドを集めてスタートするのがポイントです。</div></div>
<div class="faq-item"><div class="faq-item__q">課金しないと無理ですか？</div><div class="faq-item__a">TH7程度は完全無課金で達成できます。最初のジェム500個でビルダーを3人にすれば十分です。それ以上の課金は不要です。</div></div>
<div class="faq-item"><div class="faq-item__q">ポイントはいつ付きますか？</div><div class="faq-item__a">TH7達成後、ポイントサイトの管理画面に「未確定」として1〜3週間で反映されます。反映されない場合はサポートに問い合わせましょう。</div></div>

<h2>まとめ：最短達成の4か条</h2>
<ol>
<li><strong>ビルダーを3人にしてから建設を開始する</strong>（ジェム250個を投資）</li>
<li><strong>マルチ略奪を1日3〜5回行う</strong>（資源を積極的に略奪）</li>
<li><strong>集めたゴールドはすぐ建設に使う</strong>（貯め込まない）</li>
<li><strong>長時間の建設は寝る前にスタートする</strong>（起きたら完成）</li>
</ol>
<p>クラッシュオブクランは建設の待ち時間が長いですが、その間に略奪で資源を集めれば効率よくTH7に到達できます。Moppyで最大4,500円を狙いましょう。</p>
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
