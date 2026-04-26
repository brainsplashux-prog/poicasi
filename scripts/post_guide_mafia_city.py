# -*- coding: utf-8 -*-
"""マフィアシティ 詳細版投稿"""
import json, sys, urllib.request
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles"

ARTICLE = {
    "title": "【マフィアシティ ポイ活攻略】5日で4,000円！時給500円のマンション建設達成法",
    "slug": "mafia-city-poikatsu-guide",
    "description": "マフィアシティのポイ活攻略を完全解説。指定レベルの達成条件を5日・約8時間でクリアしてMoppyで最大4,000円を獲得する方法。マンション建設・スタミナ管理・同盟活用を操作レベルで解説。",
    "category": ["ゲーム攻略"],
    "articleType": ["game-guide"],
    "targetKeyword": "マフィアシティ ポイ活 攻略",
    "content": """
<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★☆☆☆</span><span class="game-summary-item__label">難易度（初心者OK）</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">4〜6日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約8時間</span><span class="game-summary-item__label">実質プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約500円/時</span><span class="game-summary-item__label">時給効率（Aランク）</span></div>
  </div>
</div>

<p><strong>この記事を読めばわかること：</strong>マフィアシティを一度もプレイしたことがない人でも、4〜6日・約8時間でMoppyで最大4,000円を獲得できます。「マンション（本拠地）を指定レベルにする」というシンプルな目標を、操作手順レベルで解説します。</p>

<div class="warning-box"><strong>⚠️ 始める前に必ず確認</strong><p>ポイントサイトの案件ページを経由してからダウンロードしてください。達成条件（マンションのレベル・勢力値など）は案件によって異なります。インストール直前に必ず条件を確認してください。</p></div>

<h2>ポイントサイト別 報酬比較（2026年4月時点）</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件（目安）</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>4,000円</strong></td><td>マンションLv15到達</td><td>約500円/時</td></tr>
<tr><td>ポイントインカム</td><td>3,500円</td><td>マンションLv15到達</td><td>約438円/時</td></tr>
<tr><td>ハピタス</td><td>3,000円</td><td>マンションLv15到達</td><td>約375円/時</td></tr>
</table>
<p>※条件・報酬額は随時変動します。インストール直前に必ず案件ページで確認してください。</p>

<h2>マフィアシティってどんなゲーム？</h2>
<p>マフィアシティは、マフィアのボスとして街を支配していくストラテジーゲームです。「マンション（本拠地となる建物）」を強化しながら、資源を集めて組織を成長させます。ポイ活の達成条件は「マンションを指定レベル（例：レベル15）まで上げること」です。</p>
<p>ライズオブキングダムやロードモバイルと同じジャンルで、建設・資源収集・同盟ヘルプを繰り返して進めるゲームです。同ジャンルの経験者はより短時間で達成できます。</p>

<h2>画面の基本構成（最初に覚える5つ）</h2>
<ul>
<li><strong>マンション（本拠地・街の中心）</strong>：これを指定レベルまで上げるのが目標</li>
<li><strong>ミッション（画面左のアイコン）</strong>：メインミッション。これに従って進めると資源・アイテムがもらえる</li>
<li><strong>スタミナ（画面右上のアイコン）</strong>：ギャング討伐に使用。5分に1回復・最大100</li>
<li><strong>建設メニュー（空き地をタップ）</strong>：製材所・精製所・製鉄所などの資源施設を建てる</li>
<li><strong>ギャング（画面下の盾マーク）</strong>：同盟機能。加入でヘルプをもらえる</li>
</ul>

<h2>スタミナの仕組みを理解する</h2>
<ul>
<li><strong>スタミナ最大値：</strong>100</li>
<li><strong>回復速度：</strong>5分に1回復（全回復まで約8時間20分）</li>
<li><strong>使い道：</strong>マップ上のゾンビ・敵ギャングを討伐してアイテムを入手</li>
<li><strong>推奨サイクル：</strong>朝・昼・夜の3回プレイでスタミナを消化する</li>
</ul>

<h2>インストール直後にやること（超重要）</h2>

<h3>ステップ1：チュートリアルを完了する</h3>
<p>ゲームを開くと自動でチュートリアルが始まります。画面の指示に従ってタップするだけで基本操作が学べます。チュートリアル完了後、マンションはレベル4〜5程度になっています。</p>

<h3>ステップ2：ギャング（同盟）に入る</h3>
<p>操作：画面下メニューの「ギャング（盾マーク）」→「ギャングを探す」→ 人数の多いギャングを選んで「申請」。<br>
<strong>理由：</strong>ギャングに入ると「建設ヘルプ」をもらえます。建設中の施設をタップ → 「ヘルプ要請」→ メンバーがタップするたびに建設時間が短縮されます。</p>

<h3>ステップ3：ミッションを最優先でこなす</h3>
<p>画面左のミッションアイコン → 「メインミッション」→ 上から順にクリア。<strong>迷ったらミッションの指示通りに進めるだけでOK。</strong>ミッション報酬として大量の資源・加速アイテムがもらえます。</p>

<h2>建設の優先順位</h2>
<ol>
<li><strong>製材所・精製所・製鉄所・農場</strong>（資源生産施設）を全種類建設して最大レベルまで上げる</li>
<li><strong>マンションのアップグレード条件となる施設</strong>（マンションをタップ → 「アップグレード条件」で確認）を先にレベルアップ</li>
<li><strong>マンション</strong>を条件が揃ったらすぐアップグレード</li>
</ol>

<h2>日別攻略ロードマップ</h2>

<div class="day-roadmap">
<div class="day-roadmap__title">4〜6日間の完全攻略ステップ</div>

<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（プレイ時間：約2時間）：チュートリアル完了・マンションLv5〜8</h4>
    <p><strong>◆ チュートリアル後すぐにやること</strong></p>
    <ol>
      <li>ギャング（同盟）に加入する</li>
      <li>メインミッションを上から順にこなす</li>
      <li>スタミナを使ってゾンビ討伐（マップ → ゾンビをタップ → 「討伐」）</li>
      <li>建設完了したらすぐ次の建設を開始する（ビルダーを遊ばせない）</li>
    </ol>
    <p><strong>◆ 加速アイテムの使い方</strong><br>
    建設中の施設をタップ → 「加速」→ 所持しているアイテムを選択してタップ。ギャングヘルプを受けた後に使うのが最も効率的です。</p>
    <p><strong>◆ 就寝前に長時間の建設をスタート</strong></p>
  </div>
</div>

<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2〜4（各1.5〜2時間）：マンションLv9〜13</h4>
    <p><strong>◆ 毎日のルーティン（必ず実行）</strong></p>
    <ol>
      <li>ミッション報酬を受け取る</li>
      <li>ギャングヘルプを送る（ギャング画面 → 「ヘルプ」→ メンバーの建設を支援）</li>
      <li>スタミナを全消化（マップでゾンビ・敵討伐）</li>
      <li>採集部隊を出す（マップ → 資源ポイント → 「採集」）</li>
      <li>建設が完了したら即次の建設を開始</li>
    </ol>
    <p><strong>◆ 資源不足時の対処法</strong><br>
    マップ（地球儀アイコン）→ 光っている資源ポイント（木材・鉄・食料マーク）をタップ → 「採集」→ 部隊を選んで派遣。放置で資源を自動収集してくれます。</p>
  </div>
</div>

<div class="day-step day-step--final">
  <div class="day-step__num">5</div>
  <div class="day-step__content">
    <h4>Day 5〜6：マンションLv15達成 🎉</h4>
    <p><strong>◆ 最終段階のコツ</strong><br>
    マンションLv13〜15のアップグレードには大量の資源が必要です。採集部隊を複数出しながら、温存してきた加速アイテムをここで全て投入しましょう。ギャングヘルプも積極的にもらいましょう。</p>
    <p><strong>◆ 達成確認の方法</strong><br>
    マンションをタップして「レベル15」と表示されていればOK。ポイントサイトに1〜3週間で反映されます。</p>
  </div>
</div>
</div>

<h2>よくある質問 Q&A</h2>
<div class="faq-item"><div class="faq-item__q">マンションのアップグレード条件が満たせません</div><div class="faq-item__a">マンションをタップ → 「アップグレード条件」で未達成項目を確認。赤く表示されている施設を先にレベルアップしてください。ミッションを進めると自然と条件が揃うことが多いです。</div></div>
<div class="faq-item"><div class="faq-item__q">スタミナが回復するのが遅い</div><div class="faq-item__a">5分に1回復・最大100なので全回復まで約8時間20分かかります。朝・昼・夜の3回に分けてプレイすれば効率よく消化できます。スタミナ上限を溢れさせないようにしましょう。</div></div>
<div class="faq-item"><div class="faq-item__q">課金しないと無理ですか？</div><div class="faq-item__a">完全無課金で達成できます。ミッション報酬と採集で資源を確保し、加速アイテムで建設時間を短縮すれば課金なしで十分です。</div></div>
<div class="faq-item"><div class="faq-item__q">ポイントはいつ付きますか？</div><div class="faq-item__a">達成後1〜3週間でポイントサイトの管理画面に「未確定」として反映されます。反映されない場合はスクリーンショットを添えてサポートに問い合わせてください。</div></div>

<h2>まとめ：最短達成の4か条</h2>
<ol>
<li><strong>ギャングに入ってヘルプを活用する</strong>（建設時間の大幅短縮）</li>
<li><strong>ミッションの指示通りに進める</strong>（資源・加速アイテムを効率よく入手）</li>
<li><strong>スタミナを1日3回消化する</strong>（ゾンビ討伐で加速アイテム収集）</li>
<li><strong>採集部隊を常に出しておく</strong>（放置で自動資源収集）</li>
</ol>
<p>マフィアシティは城ゲージャンルの入門として最適な難易度。コツを掴めば4〜6日でMoppy最大4,000円を無課金達成できます。</p>
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
