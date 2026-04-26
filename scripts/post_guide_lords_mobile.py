# -*- coding: utf-8 -*-
"""ロードモバイル 詳細版投稿"""
import json, sys, urllib.request
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

ARTICLE = {
    "title": "【ロードモバイル ポイ活攻略】3日で4,000円！城レベル13の最短達成法",
    "slug": "lords-mobile-poikatsu-guide",
    "description": "ロードモバイルのポイ活攻略を完全解説。城レベル13（城主レベル13）を3〜5日・約8時間で達成してMoppyで4,000円を獲得する方法。ルーキークエスト・建設優先順位・スタミナ管理を操作レベルで解説。",
    "category": ["ゲーム攻略"],
    "articleType": ["game-guide"],
    "targetKeyword": "ロードモバイル ポイ活 攻略 城レベル13",
    "content": """
<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★★☆☆</span><span class="game-summary-item__label">難易度（少し手間あり）</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">3〜5日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約8時間</span><span class="game-summary-item__label">実質プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約500円/時</span><span class="game-summary-item__label">時給効率（Aランク）</span></div>
  </div>
</div>

<p><strong>この記事を読めばわかること：</strong>ロードモバイルを初めてプレイする方でも、3〜5日・約8時間で城レベル13（城主レベル13）に到達しMoppyで最大4,000円を獲得できます。「ルーキークエスト」という初心者向けミッションが鍵で、これをこなすだけで大量の資源と加速アイテムが手に入ります。操作の手順を一つ一つ丁寧に解説します。</p>

<div class="warning-box"><strong>⚠️ 始める前に必ず確認</strong><p>ポイントサイトの案件ページを経由してからダウンロードしてください。案件によって達成条件（城レベル・ヒーロー数など）が異なります。「城レベル13到達」「ヒーロー20体入手」など条件を正確に確認してからインストールしてください。</p></div>

<h2>ポイントサイト別 報酬比較（2026年4月時点）</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件（目安）</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>4,000円</strong></td><td>城レベル13到達</td><td>約500円/時</td></tr>
<tr><td>ポイントインカム</td><td>3,500円</td><td>城レベル13到達</td><td>約438円/時</td></tr>
<tr><td>ハピタス</td><td>3,000円</td><td>城レベル13到達</td><td>約375円/時</td></tr>
</table>
<p>※条件・報酬額は随時変動します。インストール直前に必ず案件ページで確認してください。</p>

<h2>ロードモバイルってどんなゲーム？</h2>
<p>ロードモバイルは、自分の城（王国）を成長させながら他プレイヤーと争うリアルタイムストラテジーゲームです。ポイ活の達成条件は「城主レベル（城の中心となる建物のレベル）を13にすること」です。城レベルを上げるには資源（食料・木材・石材・鉄・金）が必要で、これをいかに効率よく集めるかがカギです。</p>
<p><strong>最大のポイントは「ルーキークエスト」</strong>。初心者専用のミッションで、これをこなすだけで大量の資源・加速アイテムが手に入り、自然と城レベルが上がる仕組みになっています。</p>

<h2>画面の基本構成（最初に覚える5つ）</h2>
<ul>
<li><strong>城主（城の中心建物）</strong>：これをレベル13にするのが目標。城内の一番目立つ大きな建物</li>
<li><strong>ルーキークエスト（画面左のクエストアイコン）</strong>：初心者向けミッション一覧。報酬が充実しているため最優先で進める</li>
<li><strong>スタミナ（画面右上の炎マーク）</strong>：モンスター討伐に使うエネルギー。10分に1回復、最大150</li>
<li><strong>建設メニュー（城内の空き地をタップ）</strong>：農場・伐採場・採石場などの資源施設を建てる</li>
<li><strong>ヒーロー（画面下メニューの剣マーク）</strong>：バトルや資源収集を強化するキャラクター</li>
</ul>

<h2>スタミナの仕組みを理解する</h2>
<ul>
<li><strong>スタミナ最大値：</strong>150（序盤。レベルが上がると増加）</li>
<li><strong>回復速度：</strong>10分に1回復（全回復まで約25時間）</li>
<li><strong>使い道：</strong>ワールドマップ上のモンスターを討伐するときに消費。討伐で資源・加速アイテム・ヒーロー強化素材が手に入る</li>
<li><strong>推奨サイクル：</strong>朝・昼・夜の3回プレイ。スタミナが溜まるたびにモンスターを討伐する</li>
</ul>

<h2>インストール直後にやること（超重要）</h2>

<h3>ステップ1：チュートリアルを完了する</h3>
<p>ゲームを開くと自動でチュートリアルが始まります。指示に従ってタップするだけで基本操作を学べます。チュートリアル中に城レベルが4〜5程度まで上がります。</p>

<h3>ステップ2：ルーキークエストを必ず進める（最重要）</h3>
<p><strong>操作：</strong>画面左側の「！」マーク（クエストアイコン）をタップ → 「ルーキークエスト」タブを選択 → ミッション一覧が表示される。<br>
ミッションをこなすと報酬（資源・加速アイテム）が受け取れます。<strong>迷ったらルーキークエストの指示に従って進めるだけでOK</strong>です。自然と必要な施設が建設され、城レベルが上がります。</p>

<h3>ステップ3：ギルドに入る</h3>
<p>画面下メニューの「ギルド」アイコンをタップ → 「ギルドを探す」→ 人数が多くアクティブなギルドに申請。<br>
<strong>なぜ重要か：</strong>ギルドに入ると「ギルドヘルプ」機能が使えます。建設中の施設をタップ → 「ヘルプを要請する」をタップ → ギルドメンバーがヘルプしてくれると建設時間が大幅短縮されます（最大50%短縮）。この機能なしでは達成に余計な1〜2日かかります。</p>

<h2>建設の優先順位</h2>
<p>城レベルを上げるには「城主のアップグレード条件を満たす施設のレベル」が必要です。城主をタップ → 「アップグレード」→ 「必要条件」に表示された施設を先にレベルアップしてから城主をアップします。</p>
<p>一般的な優先順位：</p>
<ol>
<li><strong>農場・伐採場・採石場・鉱山</strong>（資源生産施設）→ まず全部建設してレベルを上げる</li>
<li><strong>バラック（兵士訓練所）・病院</strong>→ 城主のアップグレード条件になることが多い</li>
<li><strong>城主</strong>→ 条件が揃ったらアップグレード</li>
</ol>
<p><strong>防衛施設（壁・タワー）は後回しでOK。</strong>ポイ活には攻撃より建設スピードが重要です。</p>

<h2>日別攻略ロードマップ</h2>

<div class="day-roadmap">
<div class="day-roadmap__title">3〜5日間の完全攻略ステップ</div>

<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（プレイ時間：約2時間）：チュートリアル完了・城レベル6〜8</h4>
    <p><strong>◆ チュートリアル後すぐにルーキークエストを開始</strong><br>
    チュートリアル完了 → 左の「！」アイコン → ルーキークエストを上から順にこなす。最初のいくつかをクリアするだけで大量の資源と加速アイテムがもらえます。</p>
    <p><strong>◆ スタミナを使ってモンスター討伐</strong><br>
    ワールドマップ（画面下の地球儀アイコン）→ 近くにいるモンスター（レベル1〜2）をタップ → 「討伐」。スタミナを消費して討伐すると加速アイテムがもらえます。加速アイテムは建設短縮に使いましょう。</p>
    <p><strong>◆ 加速アイテムの使い方</strong><br>
    建設中の施設をタップ → 「加速」ボタン → 所持している加速アイテムが表示される → 選んでタップ。ギルドヘルプを受けた後に加速アイテムを使うとさらに効果的です。</p>
    <p><strong>◆ 寝る前に長時間の建設をスタート</strong><br>
    城主のアップグレードや資源施設の建設には数時間〜1日かかります。就寝前にスタートして朝完成させましょう。</p>
  </div>
</div>

<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2〜3（各2時間）：城レベル9〜11</h4>
    <p><strong>◆ 毎日のルーティン（必ず実行）</strong></p>
    <ol>
      <li>ルーキークエストの報酬を受け取る（左の「！」→ 完了したミッションにチェック）</li>
      <li>ギルドヘルプを送る（ギルド画面 → 「ヘルプ」→ メンバーの建設を支援 → 自分にもヘルプが来やすくなる）</li>
      <li>スタミナを使い切る（ワールドマップでモンスター討伐）</li>
      <li>採集部隊を出す（ワールドマップ → 資源ポイントをタップ → 「採集」→ 部隊を派遣。放置で資源を集めてくれる）</li>
    </ol>
    <p><strong>◆ 採集で資源を自動収集する</strong><br>
    ワールドマップ（地球儀アイコン）→ 輝いているポイント（食料・木材・石材のマーク）をタップ → 「採集」→ 部隊を選択して「進軍」。数時間後に部隊が資源を持って帰還します。この操作を1日2〜3回行うと資源が安定します。</p>
  </div>
</div>

<div class="day-step day-step--final">
  <div class="day-step__num">4</div>
  <div class="day-step__content">
    <h4>Day 4〜5：城レベル12〜13達成 🎉</h4>
    <p><strong>◆ 最終段階で詰まりやすいポイント</strong><br>
    城レベル12→13のアップグレードに必要な資源が不足しやすいです。採集部隊を増やして資源を集め続けましょう。加速アイテムを温存していた場合、ここで全て使ってOKです。</p>
    <p><strong>◆ 城レベル13の確認方法</strong><br>
    城主をタップ → 建物情報に「レベル13」と表示されていれば達成。ポイントサイトの管理画面で「未確定」として1〜3週間以内に反映されます。</p>
  </div>
</div>
</div>

<h2>よくある質問 Q&A</h2>
<div class="faq-item"><div class="faq-item__q">資源が全然集まりません</div><div class="faq-item__a">採集部隊をワールドマップに出し続けることが重要です。部隊が帰還したらすぐに再派遣しましょう。また、スタミナを使ってモンスターを討伐すると加速アイテムがもらえ、建設時間を短縮できます。</div></div>
<div class="faq-item"><div class="faq-item__q">建設条件に「ヒーローが必要」と表示されます</div><div class="faq-item__a">ルーキークエストを進めると自動でヒーローがアンロックされます。クエストを順番にこなしていれば条件は自然に満たされます。</div></div>
<div class="faq-item"><div class="faq-item__q">課金しないと無理ですか？</div><div class="faq-item__a">城レベル13程度は完全無課金で達成できます。ルーキークエストで大量の無料資源・加速アイテムがもらえるため、課金なしで十分です。</div></div>
<div class="faq-item"><div class="faq-item__q">スタミナはどう管理する？</div><div class="faq-item__a">スタミナは10分に1回復・最大150です。全回復まで約25時間かかります。朝・昼・夜の3回ゲームを開いてモンスターを討伐すれば効率よく使い切れます。スタミナ回復アイテムは城レベル11以降の資源不足時に使いましょう。</div></div>
<div class="faq-item"><div class="faq-item__q">ポイントはいつ付きますか？</div><div class="faq-item__a">城レベル13達成後、ポイントサイトの管理画面に「未確定」として1〜3週間で反映されます。反映されない場合は達成時のスクリーンショットを添えてサポートに問い合わせてください。</div></div>

<h2>まとめ：最短達成の4か条</h2>
<ol>
<li><strong>ルーキークエストを最優先でこなす</strong>（大量の無料資源・加速アイテムがもらえる）</li>
<li><strong>ギルドに入ってヘルプを活用する</strong>（建設時間を最大50%短縮）</li>
<li><strong>採集部隊を常にワールドマップに出しておく</strong>（放置で資源を自動収集）</li>
<li><strong>スタミナを1日3回消化する</strong>（モンスター討伐で加速アイテムを集める）</li>
</ol>
<p>ロードモバイルはルーキークエストのおかげで、ゲーム未経験者でも3〜5日でMoppy4,000円を狙える優秀なポイ活案件です。</p>
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
