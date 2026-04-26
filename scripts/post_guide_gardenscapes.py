# -*- coding: utf-8 -*-
"""ガーデンスケイプ 詳細版投稿"""
import json, sys, urllib.request
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

ARTICLE = {
    "title": "【ガーデンスケイプ ポイ活攻略】7日でエリア解放！時給400円の達成手順",
    "slug": "gardenscapes-poikatsu-guide",
    "description": "ガーデンスケイプのポイ活攻略を完全解説。パズルの攻略コツ・星の効率的な使い方・コインの温存法まで初心者向けに操作レベルで解説。Moppyで最大3,000円・時給約400円のBランク案件。",
    "category": ["ゲーム攻略"],
    "articleType": ["game-guide"],
    "targetKeyword": "ガーデンスケイプ ポイ活 攻略",
    "content": """
<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★★☆☆</span><span class="game-summary-item__label">難易度（パズルが少し難しい）</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">5〜7日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約7〜8時間</span><span class="game-summary-item__label">実質プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約400円/時</span><span class="game-summary-item__label">時給効率（Bランク）</span></div>
  </div>
</div>

<p><strong>この記事を読めばわかること：</strong>ガーデンスケイプを一度もプレイしたことがない人でも、5〜7日・約7〜8時間でMoppyで最大3,000円を獲得する方法を操作手順レベルで解説します。マッチ3パズルのコツ・ライフ（スタミナ）管理・コインの使い道まで網羅します。</p>

<div class="warning-box"><strong>⚠️ 始める前に必ず確認</strong><p>ポイントサイトの案件ページを経由してからダウンロードしてください。達成条件は「指定エリアまでの庭の修復完了」または「レベル〇〇到達」など案件によって異なります。インストール前に必ず確認してください。</p></div>

<h2>ポイントサイト別 報酬比較（2026年4月時点）</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件（目安）</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>3,000円</strong></td><td>エリア4〜5修復完了</td><td>約400円/時</td></tr>
<tr><td>ポイントインカム</td><td>2,500円</td><td>エリア4〜5修復完了</td><td>約333円/時</td></tr>
<tr><td>ハピタス</td><td>2,000円</td><td>エリア4〜5修復完了</td><td>約267円/時</td></tr>
</table>
<p>※条件・報酬額は随時変動します。インストール直前に必ず案件ページで確認してください。</p>

<h2>ガーデンスケイプってどんなゲーム？</h2>
<p>ガーデンスケイプは、マッチ3パズル（同じ色のタイルを3つ以上並べて消す）をクリアして「星（スター）」を集め、荒れ果てた庭を修復していくゲームです。ポイ活の達成条件は「庭の指定エリアを修復すること」。パズルをクリアするたびに星が1つもらえ、星を使って庭の部分（ベンチ・池・花壇など）を修復していきます。</p>
<p><strong>ポイント：</strong>パズルに失敗しても庭の修復は取り消されません。少しずつ積み重ねていけば必ず達成できます。</p>

<h2>画面の基本構成（最初に覚える4つ）</h2>
<ul>
<li><strong>庭の画面（メイン）</strong>：修復する場所を選ぶ。修復したい箇所をタップ → 星の消費数が表示される → 星があれば「修復」</li>
<li><strong>パズル画面</strong>：庭画面の「プレイ」ボタンをタップして開始。マッチ3パズルをクリアすると星が1つもらえる</li>
<li><strong>ライフ（ハートマーク）</strong>：画面上部左。パズルに失敗すると1つ消費。最大5つ・30分に1回復</li>
<li><strong>コイン（金色の数字）</strong>：画面上部右。パズル中に手数を追加したり、ブースターを買うときに使用</li>
</ul>

<h2>ライフ（スタミナ）の仕組みを理解する</h2>
<ul>
<li><strong>ライフ最大値：</strong>5つ</li>
<li><strong>回復速度：</strong>30分に1つ回復（5つ全回復まで2時間30分）</li>
<li><strong>消費タイミング：</strong>パズルを開始するたびに1消費（クリアしても失敗しても）。ただし<strong>クリアした場合のみ星がもらえる</strong></li>
<li><strong>推奨プレイサイクル：</strong>朝・昼・夕方・夜の4回プレイ。1回あたり5ライフ（5回パズル）を消化する</li>
</ul>
<p><strong>コツ：</strong>ライフが回復するたびにプレイするのが最速。2〜3時間おきにゲームを開く習慣をつけましょう。</p>

<h2>インストール直後にやること</h2>

<h3>ステップ1：チュートリアルを完了する</h3>
<p>ゲームを開くと執事キャラクター「オースティン」がチュートリアルを案内してくれます。指示に従ってタップするだけで基本操作が覚えられます。最初の数ステージは非常に簡単です。</p>

<h3>ステップ2：コインを「手数追加」以外に使わない</h3>
<p>コインはパズル中に「手数追加（+5手）」ボタンをタップすると900コイン消費します。<strong>序盤はこれを使わないこと。</strong>コインは後半の難しいパズルのために温存しましょう。広告を見るとライフやコインがもらえる場合があるので積極的に活用します。</p>

<h3>ステップ3：庭の修復は「必要な星数が少ない箇所」から選ぶ</h3>
<p>庭の修復箇所をタップすると「★×〇」と必要な星数が表示されます。<strong>最初は星1〜2個で修復できる箇所を優先</strong>しましょう。達成条件（例：エリア4完了）に必要な修復箇所を逆算して進めると無駄がありません。</p>

<h2>パズル攻略のコツ（初心者必読）</h2>

<h3>◆ 基本：下から消すと連鎖が起きやすい</h3>
<p>画面下部のタイルを優先して消すと、上からタイルが落ちてきて自動的に連鎖（コンボ）が起きやすくなります。上から消すより下から消す方が効率的です。</p>

<h3>◆ 特殊タイル（パワーアップ）の作り方と使い方</h3>
<ul>
<li><strong>爆弾（4つ一直線に並べると出現）</strong>：タップすると周囲のタイルを一気に消せる。ボスのような障害物の近くで使うと効果的</li>
<li><strong>ロケット（L字に5つ並べると出現）</strong>：タップすると縦または横一列を全消し</li>
<li><strong>レインボーボール（同じ色を5つ以上一直線に並べると出現）</strong>：任意のタイルと組み合わせると、その色のタイルを全て消せる最強アイテム。温存してボスステージで使う</li>
</ul>

<h3>◆ 「あと〇手」でどうしても無理なとき</h3>
<p>残り手数が0になったとき「+5手を追加する（900コイン）」というポップアップが出ます。<strong>序盤（エリア1〜2）は使わず諦めてリトライ。</strong>エリア3〜4の後半など、あと少しで目標達成のときだけ使うと費用対効果が高いです。</p>

<h2>日別攻略ロードマップ</h2>

<div class="day-roadmap">
<div class="day-roadmap__title">5〜7日間の完全攻略ステップ</div>

<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（プレイ時間：約1.5時間）：チュートリアル完了・エリア1修復開始</h4>
    <p><strong>◆ チュートリアル後すぐに庭の修復を始める</strong><br>
    オースティンの指示に従って最初の修復箇所を選びます。最初の修復は無料（チュートリアル）で完了します。</p>
    <p><strong>◆ ライフを4回使い切ったら2時間待つ</strong><br>
    5ライフ全部使い切ったら（5回パズル）、次の回復（30分後）を待ちます。待っている間は他のことをして大丈夫です。</p>
    <p><strong>◆ デイリーチャレンジを確認する</strong><br>
    画面左の「！」アイコン → 「チャレンジ」タブ。毎日クリアするとボーナスコインやブースターがもらえます。</p>
  </div>
</div>

<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2〜4（各1〜1.5時間）：エリア1〜3修復完了</h4>
    <p><strong>◆ 毎日のルーティン</strong></p>
    <ol>
      <li>朝起きたらゲームを開く → ライフが5回復している → 5回パズルをプレイ</li>
      <li>昼休みにゲームを開く → ライフが2〜3回復 → 残り全部プレイ</li>
      <li>夕方にゲームを開く → 再びライフが回復 → プレイ</li>
      <li>夜寝る前に最後のライフを消化</li>
    </ol>
    <p><strong>◆ 難しいパズルで詰まったら</strong><br>
    同じステージを何度か失敗しても焦らないこと。ライフが回復したらリトライします。下部のタイルを消すことと、特殊タイル（爆弾・ロケット）を作ることを意識しましょう。</p>
    <p><strong>◆ 庭の修復ルートを確認する</strong><br>
    庭画面で全体マップを確認（ピンチアウトで縮小表示）。達成条件のエリアまでどの修復箇所が必要か把握しておくと無駄がありません。</p>
  </div>
</div>

<div class="day-step">
  <div class="day-step__num">5</div>
  <div class="day-step__content">
    <h4>Day 5〜6（各1〜1.5時間）：エリア4修復完了</h4>
    <p><strong>◆ エリア3〜4は難しいパズルが増える</strong><br>
    ここから障害物（氷・鎖・ボックスなど）が出てくるパズルが増えます。<strong>特殊タイルを障害物の隣で作って使う</strong>のが攻略の基本です。</p>
    <p><strong>◆ 温存していたコインを使っていいタイミング</strong><br>
    エリア4の修復に必要な最後のパズルで残り手数2〜3手以内で詰まった場合のみ、手数追加（900コイン）を使いましょう。</p>
  </div>
</div>

<div class="day-step day-step--final">
  <div class="day-step__num">7</div>
  <div class="day-step__content">
    <h4>Day 6〜7：達成条件のエリア修復完了 🎉</h4>
    <p><strong>◆ 達成確認の方法</strong><br>
    指定エリアの修復が全て完了すると「エリアコンプリート！」の演出が出ます。ポイントサイトの管理画面に「未確定」として1〜3週間で反映されます。</p>
  </div>
</div>
</div>

<h2>よくある質問 Q&A</h2>
<div class="faq-item"><div class="faq-item__q">同じパズルで何度も失敗します</div><div class="faq-item__a">下部から消すこと・特殊タイルを作ることを意識してください。また、パズル開始前に「ブースター（爆弾など）」を1つ使うと格段に楽になります。ブースターはデイリーチャレンジやイベントでもらえます。</div></div>
<div class="faq-item"><div class="faq-item__q">ライフが回復するのが遅くて進まない</div><div class="faq-item__a">ライフは30分に1回復（最大5）なので、2〜3時間おきにプレイするのが最効率です。友人（Facebook連携）からライフを送ってもらうこともできます。</div></div>
<div class="faq-item"><div class="faq-item__q">課金しないと無理ですか？</div><div class="faq-item__a">完全無課金で達成できます。コインを温存してエリア後半だけに使い、ブースターはデイリー報酬でコツコツ集めれば十分です。</div></div>
<div class="faq-item"><div class="faq-item__q">ポイントはいつ付きますか？</div><div class="faq-item__a">達成後1〜3週間でポイントサイトの管理画面に「未確定」として表示されます。反映されない場合はサポートに達成時刻とスクリーンショットを添えて問い合わせてください。</div></div>

<h2>まとめ：最短達成の3か条</h2>
<ol>
<li><strong>ライフを2〜3時間おきに使い切る</strong>（放置して回復を無駄にしない）</li>
<li><strong>コインは後半のエリアのために温存する</strong>（序盤で使わない）</li>
<li><strong>下部のタイルから消して特殊タイルを作る</strong>（連鎖を狙う）</li>
</ol>
<p>ガーデンスケイプはパズルの難易度次第ですが、コツを押さえれば7日以内に無課金達成できます。Moppyで最大3,000円を狙いましょう。</p>
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
