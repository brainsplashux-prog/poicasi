# -*- coding: utf-8 -*-
"""ライズオブキングダム 詳細版リライト"""
import json, sys, urllib.request
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ARTICLE_ID = "1p6xjr7vu"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles/{ARTICLE_ID}"

CONTENT = """
<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★☆☆☆</span><span class="game-summary-item__label">難易度（初心者OK）</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">3〜4日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約6.5時間</span><span class="game-summary-item__label">実質プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約615円/時</span><span class="game-summary-item__label">時給効率（Sランク）</span></div>
  </div>
</div>

<p><strong>この記事を読めばわかること：</strong>ライズオブキングダムを初めてインストールした人でも、3〜4日・約6.5時間で城レベル9（政庁レベル9）に到達し、Moppyで最大4,000円相当のポイントを獲得できます。「どの画面で何をタップするか」を一つずつ丁寧に解説します。</p>

<div class="warning-box"><strong>⚠️ 始める前に必ず確認</strong><p>必ずMoppyなどのポイントサイトの案件ページを経由してからアプリをダウンロードしてください。先にダウンロードしてしまうとポイントが付与されません。また、過去にインストールしたことがある端末は対象外になる場合があります。</p></div>

<h2>ポイントサイト別 報酬比較（2026年4月時点）</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>4,000円</strong></td><td>政庁レベル9到達</td><td>約615円/時</td></tr>
<tr><td>ポイントインカム</td><td>3,500円</td><td>政庁レベル9到達</td><td>約538円/時</td></tr>
<tr><td>ハピタス</td><td>3,200円</td><td>政庁レベル9到達</td><td>約492円/時</td></tr>
</table>
<p>→ <strong>Moppyが最もお得</strong>。報酬額は変動するため、始める直前に案件ページを確認してください。</p>

<h2>ライズオブキングダムってどんなゲーム？</h2>
<p>ライズオブキングダム（通称：ライキン）は、自分の「城（王国）」を育てて他のプレイヤーと競う、スマホ向けのストラテジー（戦略）ゲームです。ポイ活での達成条件は「政庁（城の中心となる建物）をレベル9にする」こと。建物を建てたり、兵士を増やしたりしながら城を成長させます。</p>
<p>難しそうに聞こえますが、レベル9程度ならチュートリアルの延長線上なので、ゲーム初心者でも問題なく達成できます。</p>

<h2>インストール直後にやること（最重要）</h2>

<h3>ステップ1：文明は「中国」を選ぶ</h3>
<p>ゲーム開始時に「どの文明でプレイするか」を選ぶ画面が出ます。<strong>必ず「中国」を選んでください。</strong></p>
<p>理由：中国文明は「建設速度+5%」のボーナスがあります。建設速度が上がると、施設のレベルアップにかかる時間が短縮され、最短日数で達成できます。他の文明でも達成はできますが、無駄に時間がかかります。</p>

<h3>ステップ2：ATT（アプリのトラッキング）を「許可する」に設定</h3>
<p>iPhoneの場合、アプリ起動時に「このAppがあなたのアクティビティを追跡することを許可しますか？」というポップアップが出ます。<strong>「許可する」をタップしてください。</strong>これを拒否するとポイントサイトとの連携が取れず、ポイントが付与されない場合があります。</p>

<h3>ステップ3：同盟に入る（超重要）</h3>
<p>画面下部のメニューバーに「同盟」ボタンがあります（盾のアイコン）。タップして「同盟センター」を開き、「参加する」から人数の多い同盟を探して申請しましょう。</p>
<p><strong>なぜ同盟が重要なのか？</strong>同盟に入ると、他のメンバーから「建設支援（ヘルプ）」を受けられます。ヘルプを受けると建設時間が最大50%以上短縮されます。これがないと達成に余計な1〜2日かかります。</p>

<h2>日別攻略ロードマップ（超具体的手順）</h2>

<div class="day-roadmap">
<div class="day-roadmap__title">3〜4日の完全攻略ステップ</div>

<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（プレイ時間：約2時間）：政庁レベル1〜5</h4>
    <p><strong>まず画面の見方を覚えましょう。</strong>ゲームを開くと自分の城が見えます。画面下部に5つのボタン（メイン・同盟・地図・城・メニュー）があります。</p>
    <p><strong>◆ チュートリアルを全てこなす</strong><br>
    最初は画面上に「！」マークの指示が出ます。これに従ってタップするだけでOK。チュートリアルを完了すると大量の資源と加速アイテムがもらえます。</p>
    <p><strong>◆ 建物は常に建設中の状態を維持する</strong><br>
    城内の空き地（薄い光が出ているマス）をタップ → 「建設」メニューが出る → 必要な施設を建てる、という流れです。常に何かを建設中にしておくのが鉄則。建設が終わったらすぐ次の建設を始めましょう。</p>
    <p><strong>◆ 政庁レベル5への必要条件</strong><br>
    政庁をレベルアップするには「条件となる他の施設のレベルアップ」が必要です。政庁をタップすると「次のレベルに必要なもの」が表示されます。表示された施設を先にレベルアップしてから、政庁をアップグレードしましょう。</p>
    <p><strong>◆ 夜寝る前にすること</strong><br>
    時間のかかる建設（30分〜1時間以上）を開始してから寝ましょう。朝起きたら完成しているので効率的です。</p>
  </div>
</div>

<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2（プレイ時間：約2.5時間）：政庁レベル6〜8</h4>
    <p><strong>◆ 毎日最初にやること（デイリールーティン）</strong></p>
    <ol>
      <li>同盟画面を開く → 右上の「ヘルプ」ボタンをタップ → 他のメンバーの建設を支援する（すると自分の建設にもヘルプが来やすくなる）</li>
      <li>「ミッション」アイコン（画面左側）をタップ → 達成済みのミッションから報酬を受け取る</li>
      <li>スタミナを確認（画面右上に炎マークのゲージ）→ スタミナが溜まっていたら「野蛮人狩り」に使う</li>
    </ol>
    <p><strong>◆ 野蛮人狩りでスタミナを使い切る</strong><br>
    画面左の「メイン画面」→ 地図上に「野蛮人」（モンスターのアイコン）がいます。タップして「攻撃」を選ぶとスタミナを消費して戦えます。倒すと資源（食料・木材・石材）や加速アイテムが手に入ります。スタミナの最大値は140で、5分で1回復します（つまり約11時間で全回復）。使い切らないともったいないので、1日に2〜3回プレイして消化しましょう。</p>
    <p><strong>◆ 加速アイテムを使うタイミング</strong><br>
    建設中の施設をタップ → 「加速」ボタンが出る → 所持している加速アイテム一覧が表示される。長い建設時間（1時間以上）のときに使うと効率的。同盟ヘルプを受け取った後に使うとさらに短縮効果が高い。</p>
    <p><strong>◆ 資源が足りなくなったら</strong><br>
    地図画面（下部メニューの地球儀アイコン）→ 光っている場所（資源ポイント）をタップ → 「採集」を選ぶ → 部隊を派遣する。放置しておくだけで部隊が資源を集めて帰ってきます。</p>
  </div>
</div>

<div class="day-step day-step--final">
  <div class="day-step__num">3</div>
  <div class="day-step__content">
    <h4>Day 3〜4（プレイ時間：約2時間）：政庁レベル9達成 🎉</h4>
    <p><strong>◆ 最終段階で詰まりやすいポイント</strong><br>
    政庁レベル9のアップグレードに必要な条件が揃っているか確認します。政庁をタップ → 「レベルアップ」の横にある「？」アイコン → 未達成の条件が赤く表示されます。赤い項目を先にクリアしてから政庁をレベルアップします。</p>
    <p><strong>◆ 宝石（ジェム）の使い道</strong><br>
    課金通貨の「宝石」は<strong>建設の即時完了にだけ</strong>使いましょう。ガチャや外見装飾には使わないこと。残り時間が5分以内なら宝石0個で完了できます（「無料」完了ボタンが出ます）。</p>
    <p><strong>◆ 政庁レベル9到達を確認する方法</strong><br>
    政庁をタップ → 建物の説明欄に「レベル9」と表示されていればOK。ポイントサイトの管理画面で「達成」ステータスになるまで1〜2週間かかります。焦らず待ちましょう。</p>
  </div>
</div>
</div>

<h2>よくある質問（Q&A）</h2>
<div class="faq-item"><div class="faq-item__q">課金しないとクリアできませんか？</div><div class="faq-item__a">全く課金不要です。序盤に大量の宝石・加速アイテムがもらえるので、それを使えば無課金で十分達成できます。課金を促す広告が出ても無視してOKです。</div></div>
<div class="faq-item"><div class="faq-item__q">スタミナが回復する時間は？</div><div class="faq-item__a">スタミナは5分に1ずつ回復します。最大140なので、スタミナが0になってから全回復まで約11時間40分かかります。朝起きたとき・昼休み・就寝前の3回プレイすれば常に効率よく使えます。</div></div>
<div class="faq-item"><div class="faq-item__q">建設が終わっているのに次のレベルアップができません</div><div class="faq-item__a">政庁のレベルアップには「複数の施設が一定レベル以上」という条件があります。政庁をタップして「必要条件」を確認し、未達成の施設を先にレベルアップしてください。</div></div>
<div class="faq-item"><div class="faq-item__q">ポイントはいつ付与されますか？</div><div class="faq-item__a">達成後、ポイントサイトの管理画面に反映されるまで通常1〜3週間かかります。「未確定」→「確定」→「交換可能」の順に変わります。</div></div>

<h2>まとめ：最短達成のための3つのポイント</h2>
<ol>
<li><strong>最初に「中国」文明を選ぶ</strong>（建設速度+5%）</li>
<li><strong>同盟に入ってヘルプを活用する</strong>（建設時間が大幅短縮）</li>
<li><strong>常に建設中の状態を維持し、スタミナを使い切る</strong>（1日3回プレイ）</li>
</ol>
<p>この3点さえ守れば、ゲーム初心者でも3〜4日でMoppy最大4,000円を獲得できます。</p>
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
    print("ライズオブキングダム 詳細版リライト中...")
    patch_article(CONTENT)
    print("完了")
