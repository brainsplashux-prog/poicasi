# -*- coding: utf-8 -*-
"""ドラゴンシティ 詳細版リライト"""
import json, sys, urllib.request
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ARTICLE_ID = "1n3kjnnt4"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles/{ARTICLE_ID}"

CONTENT = """
<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★☆☆☆</span><span class="game-summary-item__label">難易度（初心者OK）</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">4〜5日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約7時間</span><span class="game-summary-item__label">実質プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約500円/時</span><span class="game-summary-item__label">時給効率（Aランク）</span></div>
  </div>
</div>

<p><strong>この記事を読めばわかること：</strong>ドラゴンシティを一度もプレイしたことがない人でも、4〜5日・約7時間でドラゴン孵化3体の条件を達成し、Moppyで最大3,500円相当のポイントを獲得する方法を画面の操作レベルで解説します。</p>

<div class="warning-box"><strong>⚠️ 始める前に必ず確認</strong><p>ポイントサイトの案件ページを踏んでからアプリをダウンロードしてください。先にダウンロード済みの端末、または過去にインストールしたことがある端末は対象外になる場合があります。</p></div>

<h2>ポイントサイト別 報酬比較（2026年4月時点）</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>3,500円</strong></td><td>ドラゴン3体孵化</td><td>約500円/時</td></tr>
<tr><td>ポイントインカム</td><td>3,000円</td><td>ドラゴン3体孵化</td><td>約429円/時</td></tr>
</table>
<p>※案件の条件はポイントサイトによって異なる場合があります。必ず案件ページで「達成条件」を確認してから始めてください。</p>

<h2>ドラゴンシティってどんなゲーム？</h2>
<p>ドラゴンシティは、島の上にドラゴンの巣を作り、ドラゴンを育てて繁殖させるファンタジー系の放置育成ゲームです。ポイ活での目標は「3体のドラゴンを孵化させること」。ドラゴンを2体かけ合わせると卵が生まれ、時間が経つと孵化します。この孵化を3回繰り返すだけです。</p>
<p><strong>最大のポイントは「待ち時間が長い＝放置でOK」ということ。</strong>孵化には数時間〜最大1日かかりますが、その間は何もしなくていいので、実質の操作時間は非常に短いです。</p>

<h2>画面の基本構成（最初に覚えること）</h2>
<p>ゲームを開くと、島の上に建物とドラゴンが見えます。画面下部に5つのメニューがあります。</p>
<ul>
<li><strong>「島」</strong>：メイン画面。建物を建てたりドラゴンを確認する</li>
<li><strong>「市場」</strong>：建物や卵を購入する（ジェムまたはゴールドで購入）</li>
<li><strong>「目標」</strong>（左側に！マークで表示）：クエスト一覧。これを進めると報酬がもらえる</li>
<li><strong>「タワー」</strong>：毎日タップするだけでジェムがもらえるデイリーボーナス</li>
<li><strong>「バトル」</strong>：他のプレイヤーと戦う（ポイ活には必須ではない）</li>
</ul>

<h2>インストール直後にやること</h2>

<h3>ステップ1：チュートリアルに従う</h3>
<p>最初に黄色い吹き出し（ゼウスというキャラクターが説明してくれる）が表示されます。指示に従ってタップするだけで基本操作が覚えられます。チュートリアル中に最初の炎ドラゴンが孵化します（<strong>これが孵化1体目にカウントされます</strong>）。</p>

<h3>ステップ2：ジェムを孵化スロット拡張に使う</h3>
<p>最初にもらえるジェム（青い宝石）は「孵化場のスロット拡張」に使いましょう。孵化場をタップ → 「スロットを追加」ボタン → ジェムを使って追加。スロットが多いほど複数の卵を同時に孵化できます。</p>
<p><strong>ガチャ（ドラゴン購入）にジェムを使わないこと</strong>が重要です。</p>

<h2>日別攻略ロードマップ（超具体的手順）</h2>

<div class="day-roadmap">
<div class="day-roadmap__title">4〜5日間の完全攻略ステップ</div>

<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（プレイ時間：約2時間）：1体目の孵化 ＋ 2体目の準備</h4>
    <p><strong>◆ チュートリアルで1体目が孵化（自動）</strong><br>
    チュートリアルを進めると炎ドラゴン（Fire Dragon）が孵化します。これで孵化1体達成です。</p>
    <p><strong>◆ 農園を増やしてエサを確保する</strong><br>
    ドラゴンを育てるには「エサ（食料）」が必要です。島の空いているスペースをタップ → 「建設」→「農園」を建設する。農園は収穫までの時間が短いものから順に選ぶと効率的（1分で収穫できる小さい農園が序盤は便利）。</p>
    <p><strong>◆ 交配マウンテン（育種所）を使って2体目の卵を作る</strong><br>
    操作手順：島内の「交配マウンテン」（山の形の建物）をタップ → 「交配する」をタップ → 左右に親ドラゴンを1体ずつ選ぶ（初期の炎ドラゴンと、チュートリアルでもらった別のドラゴン）→「交配スタート」。交配には数時間かかります（<strong>この間は放置でOK</strong>）。</p>
    <p><strong>◆ 夜寝る前に交配をスタートさせる</strong><br>
    交配には平均4〜8時間かかります。就寝前にスタートしておくと翌朝に卵が完成します。</p>
  </div>
</div>

<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2（プレイ時間：約1.5時間）：2体目の孵化 ＋ 3体目の準備</h4>
    <p><strong>◆ 毎日やるデイリーボーナスを受け取る（所要5分）</strong></p>
    <ol>
      <li>「ドラゴンタワー」をタップ → 毎日タップするだけでジェムがもらえる（連続でタップすると報酬が増える）</li>
      <li>「ドラゴンTV」をタップ → 広告動画を見るとジェムやエサがもらえる（1日数回まで）</li>
      <li>画面左の「！」マーク（目標）をタップ → 達成済みのクエストから報酬を受け取る</li>
    </ol>
    <p><strong>◆ 昨夜の卵を孵化場に移して孵化させる</strong><br>
    交配マウンテンをタップ → 「卵を受け取る」ボタン → 孵化場に移動 → 「孵化開始」をタップ。孵化にも数時間〜1日かかります。</p>
    <p><strong>◆ すぐに次の交配をスタートする</strong><br>
    卵を受け取ったら、交配マウンテンが空きます。すぐに新しい交配（3体目用）をスタートしましょう。異なる属性のドラゴンを組み合わせると珍しいドラゴンが生まれることがあります（ポイ活には関係ないので何でもOK）。</p>
  </div>
</div>

<div class="day-step">
  <div class="day-step__num">3</div>
  <div class="day-step__content">
    <h4>Day 3〜4（プレイ時間：約2時間）：2体目孵化完了 ＋ 3体目の孵化待ち</h4>
    <p><strong>◆ 孵化場を確認する</strong><br>
    孵化場をタップ → 残り時間が表示されます。ゲージが100%になったら「孵化完了！」の通知が届きます。タップすると2体目のドラゴンが誕生します。</p>
    <p><strong>◆ ドラゴンにエサをあげてレベルを上げておく</strong><br>
    孵化待ちの時間に、既存のドラゴンにエサをあげてレベルを上げておくと後で役立ちます。ドラゴンをタップ → 「エサ」をタップ → エサを選んで与える。</p>
    <p><strong>◆ ジェムを孵化時間の短縮に使う場合</strong><br>
    孵化場をタップ → 「今すぐ完了」ボタン → 必要なジェム数が表示されます。残り時間が1時間以内なら少ないジェムで完了できます。急がない場合は待てばOK。</p>
  </div>
</div>

<div class="day-step day-step--final">
  <div class="day-step__num">5</div>
  <div class="day-step__content">
    <h4>Day 4〜5：3体目孵化で達成完了 🎉</h4>
    <p>3体目の卵が孵化すれば条件達成です。孵化完了の通知が来たらタップして「3体目のドラゴン誕生」を確認しましょう。</p>
    <p><strong>達成確認の方法：</strong>ポイントサイトの「獲得予定ポイント」欄に反映されるまで1〜2週間かかります。管理画面で「未確定」と表示されていれば、正しく計測されています。</p>
  </div>
</div>
</div>

<h2>詰まりやすいポイントQ&A</h2>
<div class="faq-item"><div class="faq-item__q">交配中に「孵化場がいっぱい」と出て卵を受け取れません</div><div class="faq-item__a">孵化場のスロットが埋まっています。既存の卵の孵化が完了してからドラゴンを巣に移動させ、スロットを空けてから卵を受け取りましょう。または、ジェムでスロットを追加できます。</div></div>
<div class="faq-item"><div class="faq-item__q">交配の待ち時間が24時間以上あります</div><div class="faq-item__a">珍しいドラゴンの組み合わせほど時間がかかります。待つか、ジェムで短縮するか選べます。急ぐ場合は基本属性（炎・水・草など）のドラゴン同士を交配すると時間が短くなる傾向があります。</div></div>
<div class="faq-item"><div class="faq-item__q">課金しないと進めませんか？</div><div class="faq-item__a">全く不要です。ジェムはデイリーボーナスや広告視聴で無料で集まります。孵化3体という条件は無課金で十分達成できます。</div></div>
<div class="faq-item"><div class="faq-item__q">スタミナ（バトルエネルギー）はどう管理する？</div><div class="faq-item__a">バトルエネルギーは15分で1回復します。バトルはポイ活条件に含まれないことが多いので、無理に消化しなくてOKです。ただし、バトルをすると経験値やジェムが手に入るので、余裕があれば活用しましょう。</div></div>

<h2>まとめ：達成のための3ステップ</h2>
<ol>
<li><strong>チュートリアルで1体目を孵化</strong>（自動で完了）</li>
<li><strong>夜寝る前に交配をスタート → 翌朝卵を孵化場へ移す</strong>を繰り返す</li>
<li><strong>デイリーボーナスを毎日受け取り、ジェムを孵化短縮に温存</strong></li>
</ol>
<p>「常に何かを孵化中」の状態を保つのがコツ。4〜5日間の放置時間を上手く使えば、実質の操作は1日30分程度で達成できます。</p>
<div class="cta-box"><div class="cta-box__title">ゲームしながらポイントを貯めるなら「ポイカジ」も！</div><p class="cta-box__desc">30秒で遊べるカジュアルゲームで毎日コツコツ。複数のポイ活を掛け持ちするとさらにお得です。</p><a href="https://poicasi.co.jp" class="cta-box__btn" target="_blank" rel="noopener">ポイカジを始める →</a></div>
"""

def patch_article(content):
    body = json.dumps({"content": content}, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=body,
        headers={"X-MICROCMS-API-KEY": API_KEY, "Content-Type": "application/json"},
        method="PATCH",
    )
    with urllib.request.urlopen(req) as res:
        result = json.loads(res.read())
        print(f"[OK] 更新成功: ID={result.get('id')}")

if __name__ == "__main__":
    print("ドラゴンシティ 詳細版リライト中...")
    patch_article(CONTENT)
    print("完了")
