# -*- coding: utf-8 -*-
"""バイキングライズ 詳細版投稿"""
import json, sys, urllib.request
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

ARTICLE = {
    "title": "【バイキングライズ ポイ活攻略】5日で4,500円！時給560円の城レベル達成法",
    "slug": "viking-rise-poikatsu-guide",
    "description": "バイキングライズのポイ活攻略を完全解説。城レベル達成条件を5日・約8時間でクリアしてMoppyで最大4,500円を獲得する方法。建設優先順位・スタミナ管理・同盟ヘルプの活用を操作レベルで解説。",
    "category": ["ゲーム攻略"],
    "articleType": ["game-guide"],
    "targetKeyword": "バイキングライズ ポイ活 攻略",
    "content": """
<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★☆☆☆</span><span class="game-summary-item__label">難易度（初心者OK）</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">4〜6日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約8時間</span><span class="game-summary-item__label">実質プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約560円/時</span><span class="game-summary-item__label">時給効率（Aランク）</span></div>
  </div>
</div>

<p><strong>この記事を読めばわかること：</strong>バイキングライズを初めてプレイする方でも、4〜6日・約8時間で城レベル達成条件をクリアしてMoppyで最大4,500円を獲得する方法を操作レベルで解説します。ライキン（ライズオブキングダム）と似た城ゲーなので、ライキン経験者はさらに短時間で達成できます。</p>

<div class="warning-box"><strong>⚠️ 始める前に必ず確認</strong><p>ポイントサイトの案件ページを経由してからダウンロードしてください。達成条件（城レベルの数値）は案件によって異なります。インストール直前に必ず条件を確認してください。</p></div>

<h2>ポイントサイト別 報酬比較（2026年4月時点）</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件（目安）</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>4,500円</strong></td><td>城レベル16到達</td><td>約560円/時</td></tr>
<tr><td>ポイントインカム</td><td>4,000円</td><td>城レベル16到達</td><td>約500円/時</td></tr>
<tr><td>ハピタス</td><td>3,500円</td><td>城レベル16到達</td><td>約438円/時</td></tr>
</table>
<p>※条件・報酬額は随時変動します。インストール直前に必ず案件ページで確認してください。</p>

<h2>バイキングライズってどんなゲーム？</h2>
<p>バイキングライズはバイキング（北欧の海賊）をテーマにした城建設ストラテジーゲームです。ライズオブキングダム（ライキン）と非常によく似たゲームで、自分の城（砦）を建設・強化して他プレイヤーと戦います。ポイ活の達成条件は「砦（城）を指定のレベルにすること」です。</p>
<p><strong>ライキン経験者へ：</strong>操作感はほぼ同じです。同盟ヘルプ・資源採集・加速アイテムの使い方も同様です。</p>

<h2>画面の基本構成（最初に覚える5つ）</h2>
<ul>
<li><strong>砦（城の中心建物）</strong>：これを指定レベルまで上げるのが目標。城内の中央にある最大の建物</li>
<li><strong>クエスト（画面左のアイコン）</strong>：メインクエスト。これに従って進めると資源・加速アイテムがもらえる</li>
<li><strong>スタミナ（画面右上の稲妻マーク）</strong>：モンスター討伐に使う。6分に1回復・最大120</li>
<li><strong>建設メニュー（空き地をタップ）</strong>：農場・木こり小屋・採石場などの資源施設を建てる</li>
<li><strong>同盟（画面下の盾マーク）</strong>：加入すると建設ヘルプをもらえる。序盤から必ず入ること</li>
</ul>

<h2>スタミナの仕組みを理解する</h2>
<ul>
<li><strong>スタミナ最大値：</strong>120</li>
<li><strong>回復速度：</strong>6分に1回復（全回復まで約12時間）</li>
<li><strong>使い道：</strong>ワールドマップのモンスター討伐。討伐で資源・加速アイテムが手に入る</li>
<li><strong>推奨サイクル：</strong>朝・昼・夜の3回プレイでスタミナを使い切る</li>
</ul>

<h2>インストール直後にやること（超重要）</h2>

<h3>ステップ1：チュートリアルを完了する</h3>
<p>ゲームを開くと自動でチュートリアルが始まります。画面の指示に従うだけで基本操作が習得でき、砦レベルが4〜5程度まで上がります。</p>

<h3>ステップ2：同盟に入る（最優先）</h3>
<p>操作：画面下メニューの「同盟（盾マーク）」→ 「同盟に参加する」→ 人数の多い同盟を選んで「申請」。<br>
<strong>理由：</strong>同盟に入ると「建設ヘルプ」が使えます。建設中の施設をタップ → 「ヘルプを要請」→ メンバーがタップするたびに建設時間が短縮（1回あたり数分〜数十分）。10〜20人のヘルプで長時間建設が数時間短縮されます。これなしでは1〜2日余計にかかります。</p>

<h3>ステップ3：メインクエストを最優先で進める</h3>
<p>画面左のクエストアイコン → 「メインクエスト」タブ → 上から順にクリアしていく。<strong>迷ったらクエストの指示通りに進めればOK。</strong>クエストをこなすだけで大量の資源と加速アイテムがもらえ、自然と砦レベルが上がります。</p>

<h2>建設の優先順位</h2>
<ol>
<li><strong>農場・木こり小屋・採石場・鉱山</strong>（資源施設）を全種類建設してレベルを上げる</li>
<li><strong>砦のアップグレード条件となる施設</strong>（砦をタップ → 「アップグレード」→ 「条件」で確認）を先にレベルアップ</li>
<li><strong>砦</strong>を条件が揃ったらすぐアップグレード</li>
</ol>
<p>防衛施設（壁など）は後回しでOKです。</p>

<h2>日別攻略ロードマップ</h2>

<div class="day-roadmap">
<div class="day-roadmap__title">4〜6日間の完全攻略ステップ</div>

<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（プレイ時間：約2時間）：チュートリアル完了・砦レベル6〜8</h4>
    <p><strong>◆ チュートリアル直後にやること</strong></p>
    <ol>
      <li>同盟に入る（盾マーク → 参加）</li>
      <li>クエストを上から順にこなす</li>
      <li>スタミナを使ってモンスター討伐（ワールドマップ → モンスターをタップ → 討伐）</li>
      <li>加速アイテムを建設に使う（建設中の施設をタップ → 「加速」→ アイテム選択）</li>
    </ol>
    <p><strong>◆ 寝る前に長時間の建設を開始する</strong><br>
    砦のアップグレードや主要施設の建設は数時間かかります。就寝前にスタートして朝完成させましょう。同盟ヘルプを受けてから寝るとさらに効率的です。</p>
  </div>
</div>

<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2〜4（各1.5〜2時間）：砦レベル9〜13</h4>
    <p><strong>◆ 毎日のルーティン</strong></p>
    <ol>
      <li>クエスト報酬を受け取る（左アイコン → 完了クエストから受け取り）</li>
      <li>同盟ヘルプを送る（同盟 → 「ヘルプ」→ メンバーの建設を支援）</li>
      <li>スタミナを全消化（ワールドマップでモンスター討伐 × 複数回）</li>
      <li>採集部隊を出す（ワールドマップ → 資源ポイント → 「採集」→ 部隊派遣）</li>
      <li>建設が完了していたら次の建設をすぐ開始する</li>
    </ol>
    <p><strong>◆ 資源が足りなくなったら</strong><br>
    ワールドマップの資源ポイント（食料・木材などのアイコン）をタップ → 「採集」→ 部隊を選んで派遣。数時間放置するだけで部隊が資源を集めて帰ってきます。</p>
  </div>
</div>

<div class="day-step day-step--final">
  <div class="day-step__num">5</div>
  <div class="day-step__content">
    <h4>Day 5〜6：砦レベル16達成 🎉</h4>
    <p><strong>◆ 最終段階のコツ</strong><br>
    砦レベル14〜16のアップグレードには大量の資源が必要です。採集部隊を複数出して資源を集めながら、加速アイテムを惜しまず使いましょう。</p>
    <p><strong>◆ 達成確認の方法</strong><br>
    砦をタップして「レベル16」と表示されていればOK。ポイントサイトに1〜3週間で反映されます。</p>
  </div>
</div>
</div>

<h2>よくある質問 Q&A</h2>
<div class="faq-item"><div class="faq-item__q">砦のレベルアップ条件が揃っているのにアップできません</div><div class="faq-item__a">資源（食料・木材・石材・鉄）が不足している可能性があります。砦をタップ → 「アップグレード」→ 不足している資源が赤く表示されます。採集部隊を出して補充しましょう。</div></div>
<div class="faq-item"><div class="faq-item__q">スタミナが全回復するのに12時間かかります</div><div class="faq-item__a">6分に1回復なので、朝・昼・夜の3回ゲームを開いてスタミナを使い切るのが最効率です。スタミナ上限120を溢れさせないよう、こまめに消化しましょう。</div></div>
<div class="faq-item"><div class="faq-item__q">課金しないと無理ですか？</div><div class="faq-item__a">完全無課金で達成できます。クエスト報酬と採集で資源を集め、加速アイテムを活用すれば課金なしで十分です。</div></div>
<div class="faq-item"><div class="faq-item__q">ポイントはいつ付きますか？</div><div class="faq-item__a">達成後1〜3週間でポイントサイトの管理画面に「未確定」として反映されます。</div></div>

<h2>まとめ：最短達成の4か条</h2>
<ol>
<li><strong>すぐに同盟に入ってヘルプを活用する</strong>（建設時間を大幅短縮）</li>
<li><strong>メインクエストの指示に従う</strong>（大量の資源・加速アイテムがもらえる）</li>
<li><strong>スタミナを1日3回消化する</strong>（モンスター討伐で加速アイテム収集）</li>
<li><strong>採集部隊を常に出しておく</strong>（放置で自動資源収集）</li>
</ol>
<p>バイキングライズはライキンと同様の城ゲーで、コツを掴めば4〜6日でMoppy最大4,500円を達成できます。</p>
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
