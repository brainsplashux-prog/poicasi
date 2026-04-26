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
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">4〜6日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約7時間</span><span class="game-summary-item__label">実質プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約571円/時</span><span class="game-summary-item__label">時給効率（Aランク）</span></div>
  </div>
</div>

<p><strong>この記事を読めばわかること：</strong>ファイナルギアを初めてプレイする方でも、4〜6日・約7時間でMoppyで最大4,000円を獲得できます。拠点レベルを指定数まで上げる手順をスタミナ管理・建設優先順位まで操作レベルで解説します。</p>

<div class="warning-box"><strong>⚠️ 始める前に必ず確認</strong><p>ポイントサイトの案件ページを経由してからダウンロードしてください。達成条件（拠点レベル・司令官レベルなど）は案件によって異なります。インストール直前に必ず確認してください。</p></div>

<h2>ポイントサイト別 報酬比較（2026年4月時点）</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件（目安）</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>4,000円</strong></td><td>拠点レベル15到達</td><td>約571円/時</td></tr>
<tr><td>ポイントインカム</td><td>3,500円</td><td>拠点レベル15到達</td><td>約500円/時</td></tr>
</table>
<p>※条件・報酬額は随時変動します。インストール直前に必ず案件ページで確認してください。</p>

<h2>ファイナルギアってどんなゲーム？</h2>
<p>ファイナルギアは、メカ（機械兵器）を操る女性パイロット「ギア」たちを育成して戦うRPGストラテジーゲームです。アニメ風のキャラクターと機械兵器の組み合わせが特徴で、日本で人気の高いジャンルです。ポイ活の目標は「拠点（基地）を指定レベルまで上げること」。建設・資源収集・バトルを繰り返してレベルを上げます。</p>

<h2>画面の基本構成</h2>
<ul>
<li><strong>拠点（画面中央の基地）</strong>：これを指定レベルにするのが目標</li>
<li><strong>ミッション（画面左のアイコン）</strong>：メインミッション。指示通りに進めると資源・アイテムがもらえる</li>
<li><strong>スタミナ（画面右上）</strong>：バトル・討伐に使用。6分に1回復・最大120</li>
<li><strong>ギルド（画面下）</strong>：加入すると建設ヘルプをもらえる</li>
</ul>

<h2>スタミナ管理</h2>
<ul>
<li><strong>最大値：</strong>120 / <strong>回復速度：</strong>6分に1回復（全回復約12時間）</li>
<li><strong>推奨サイクル：</strong>朝・昼・夜の3回でスタミナを消化</li>
<li><strong>使い道：</strong>敵キャンプへの攻撃・素材収集バトルで資源・アイテム入手</li>
</ul>

<h2>インストール直後にやること</h2>
<h3>ステップ1：チュートリアルを完了する</h3>
<p>アニメ風のストーリーが流れます。スキップしても構いません（右上の「スキップ」ボタン）。チュートリアルで拠点がレベル4〜5程度になります。</p>

<h3>ステップ2：ギルドに入る</h3>
<p>画面下のギルドアイコン → 「ギルドを探す」→ 人数の多いギルドに申請。建設ヘルプで建設時間を大幅短縮できます。</p>

<h3>ステップ3：メインミッションを最優先で進める</h3>
<p>画面左のミッションアイコン → 「メインミッション」→ 上から順にクリア。大量の資源・アイテムがもらえます。</p>

<h2>建設の優先順位</h2>
<ol>
<li>資源施設（油田・鉄鉱山・部品工場など）を全種類建設してレベルアップ</li>
<li>拠点のアップグレード条件施設（拠点をタップ → 「条件」で確認）を先にレベルアップ</li>
<li>拠点を条件が揃ったらすぐアップグレード</li>
</ol>

<h2>日別攻略ロードマップ</h2>
<div class="day-roadmap">
<div class="day-roadmap__title">4〜6日間の完全攻略ステップ</div>
<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（約2時間）：チュートリアル完了・拠点レベル7〜9</h4>
    <p>チュートリアル後すぐにギルド加入 → ミッション消化 → スタミナで敵キャンプ討伐 → 加速アイテムで建設短縮 → 就寝前に長時間建設スタート。</p>
  </div>
</div>
<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2〜4（各1.5〜2時間）：拠点レベル10〜13</h4>
    <p><strong>毎日のルーティン：</strong></p>
    <ol>
      <li>ミッション報酬を受け取る</li>
      <li>ギルドヘルプを送ってから要請する</li>
      <li>スタミナを全消化（敵キャンプ討伐）</li>
      <li>採集部隊をマップに出す</li>
      <li>建設完了したら即次の建設を開始</li>
    </ol>
  </div>
</div>
<div class="day-step day-step--final">
  <div class="day-step__num">5</div>
  <div class="day-step__content">
    <h4>Day 5〜6：拠点レベル15達成 🎉</h4>
    <p>拠点13〜15は資源が多く必要です。採集部隊を複数出しながら、温存した加速アイテムを全投入。拠点をタップして「レベル15」と表示されれば達成。ポイントサイトに1〜3週間で反映されます。</p>
  </div>
</div>
</div>

<h2>よくある質問 Q&A</h2>
<div class="faq-item"><div class="faq-item__q">ギアのキャラクターは強化しないといけませんか？</div><div class="faq-item__a">拠点レベル達成が目的の場合、キャラクター強化は必須ではありません。ただし、敵キャンプの討伐に必要な場合は最低限の強化をしましょう。ミッション報酬でもらえる素材で十分です。</div></div>
<div class="faq-item"><div class="faq-item__q">スタミナが全回復するのに時間がかかります</div><div class="faq-item__a">6分に1回復・最大120なので全回復まで約12時間かかります。朝・昼・夜の3回プレイで効率よく消化しましょう。スタミナ上限を溢れさせないよう注意してください。</div></div>
<div class="faq-item"><div class="faq-item__q">課金しないと無理ですか？</div><div class="faq-item__a">完全無課金で達成できます。ミッション報酬とギルドヘルプを活用すれば課金不要です。</div></div>
<div class="faq-item"><div class="faq-item__q">ポイントはいつ付きますか？</div><div class="faq-item__a">達成後1〜3週間でポイントサイトに「未確定」として反映されます。</div></div>

<h2>まとめ：最短達成の4か条</h2>
<ol>
<li><strong>ギルドに入ってヘルプを活用する</strong></li>
<li><strong>ミッションの指示通りに進める</strong></li>
<li><strong>スタミナを1日3回消化する</strong></li>
<li><strong>採集部隊を常に出しておく</strong></li>
</ol>
<div class="cta-box"><div class="cta-box__title">ゲームしながらポイントを貯めるなら「ポイカジ」も！</div><p class="cta-box__desc">30秒で遊べるカジュアルゲームで毎日コツコツ。複数のポイ活を掛け持ちするとさらにお得です。</p><a href="https://poicasi.co.jp" class="cta-box__btn" target="_blank" rel="noopener">ポイカジを始める →</a></div>"""

ARTICLE = {
    "title": "【ファイナルギア ポイ活攻略】6日で4,000円！時給571円の拠点レベル達成法",
    "slug": "final-gear-poikatsu-guide",
    "description": "ファイナルギアのポイ活攻略。拠点レベル15到達を4〜6日・約7時間で達成してMoppyで4,000円を獲得する方法を操作レベルで解説。",
    "category": ["ゲーム攻略"],
    "articleType": ["game-guide"],
    "targetKeyword": "ファイナルギア ポイ活 攻略",
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
