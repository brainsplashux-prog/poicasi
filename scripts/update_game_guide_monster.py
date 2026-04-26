# -*- coding: utf-8 -*-
"""モンスターバスケット 詳細版リライト"""
import json, sys, urllib.request
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SERVICE_DOMAIN = "07lzrpng23"
API_KEY = "pLlZWc7f1uzCwFEtH8PvgswP7ALF7AEpASsH"
ARTICLE_ID = "wzi3fflih0a"
ENDPOINT = f"https://{SERVICE_DOMAIN}.microcms.io/api/v1/articles/{ARTICLE_ID}"

CONTENT = """
<div class="game-summary-box">
  <div class="game-summary-box__title">攻略サマリー</div>
  <div class="game-summary-grid">
    <div class="game-summary-item"><span class="game-summary-item__icon">⭐</span><span class="game-summary-item__value">★★★☆☆</span><span class="game-summary-item__label">難易度（少し手間がかかる）</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">📅</span><span class="game-summary-item__value">5〜7日</span><span class="game-summary-item__label">達成日数</span></div>
    <div class="game-summary-item"><span class="game-summary-item__icon">⏱️</span><span class="game-summary-item__value">約9時間</span><span class="game-summary-item__label">実質プレイ時間</span></div>
    <div class="game-summary-item game-summary-item--highlight"><span class="game-summary-item__icon">⚡</span><span class="game-summary-item__value">約480円/時</span><span class="game-summary-item__label">時給効率（Aランク）</span></div>
  </div>
</div>

<p><strong>この記事を読めばわかること：</strong>モンスターバスケットをインストールしたことがない人でも、5〜7日・約9時間でプレイヤーランク20に到達してMoppy最大4,500円を獲得するための具体的な操作手順を解説します。スタミナの使い方・毎日のルーティン・詰まりやすいポイントまで徹底カバーします。</p>

<div class="warning-box"><strong>⚠️ 始める前に必ず確認</strong><p>Moppyなどのポイントサイトの案件ページを踏んでからダウンロードしてください。過去にインストールしたことがある端末は対象外になる場合があります。iPhoneはATT（トラッキング許可）を「許可する」に設定してください。</p></div>

<h2>ポイントサイト別 報酬比較（2026年4月時点）</h2>
<table class="pointsite-table">
<tr><th>サイト名</th><th>報酬額</th><th>達成条件</th><th>時給効率</th></tr>
<tr class="pointsite-table__best"><td><strong>Moppy</strong></td><td class="pointsite-table__reward-high"><strong>4,500円</strong></td><td>プレイヤーランク20</td><td>約480円/時</td></tr>
<tr><td>ポイントインカム</td><td>4,000円</td><td>プレイヤーランク20</td><td>約444円/時</td></tr>
<tr><td>げん玉</td><td>3,800円</td><td>プレイヤーランク20</td><td>約422円/時</td></tr>
</table>

<h2>モンスターバスケットってどんなゲーム？</h2>
<p>モンスターバスケットは、集めたモンスターキャラクターを育ててバトルリーグで戦わせるRPGゲームです。「プレイヤーランク20」が目標で、バトルをこなして経験値を稼ぎ、ランクを上げていきます。</p>
<p>毎日コツコツとスタミナを使い切るのが最短達成のカギです。1日1.5〜2時間のプレイを5〜7日続けることで達成できます。</p>

<h2>ゲームの基本画面と操作（インストール直後）</h2>
<p>アプリを開くとメインメニューが表示されます。主に使う画面は以下の4つです。</p>
<ul>
<li><strong>「ホーム」</strong>：メイン画面。デイリーミッション・お知らせ・スタミナ確認</li>
<li><strong>「バトル」（剣のアイコン）</strong>：ストーリーや対戦バトルを選べる。ここで経験値を稼ぐ</li>
<li><strong>「モンスター」（モンスターのアイコン）</strong>：持っているモンスターの管理・強化</li>
<li><strong>「ショップ」</strong>：アイテムや装備を購入。序盤はほぼ使わない</li>
</ul>
<p><strong>スタミナの確認方法：</strong>ホーム画面の右上または上部バーに「雷マーク」のアイコンがあります。これがスタミナ（AP）です。数字が表示されていて、バトルするたびに消費します。</p>

<h2>スタミナ（AP）の仕組みを理解する</h2>
<p>このゲームで最も重要なのがスタミナ管理です。</p>
<ul>
<li><strong>スタミナ最大値：</strong>序盤は60〜80程度（ランクが上がると増える）</li>
<li><strong>回復速度：</strong>5分に1回復（つまり全回復まで約5〜7時間）</li>
<li><strong>消費量：</strong>バトル1回につき5〜15消費（ステージによって異なる）</li>
<li><strong>スタミナ回復アイテムの使い方：</strong>ホーム → アイテムバッグ → 「スタミナ回復薬」を使うと即時回復</li>
</ul>
<p><strong>理想的なプレイサイクル：</strong>朝・昼・夜の3回ゲームを開いてスタミナを使い切る。スタミナが0になったら回復アイテムを使って追加バトル。これを毎日続けます。</p>

<h2>日別攻略ロードマップ（超具体的手順）</h2>

<div class="day-roadmap">
<div class="day-roadmap__title">5〜7日間の完全攻略ステップ</div>

<div class="day-step">
  <div class="day-step__num">1</div>
  <div class="day-step__content">
    <h4>Day 1（プレイ時間：約1.5時間）：チュートリアル〜ランク5</h4>
    <p><strong>◆ チュートリアルを全てこなす</strong><br>
    最初に「チュートリアル」が始まります。画面の指示通りにタップするだけで進みます。序盤は負けることはないので気軽に進めましょう。チュートリアル完了でランク3〜4程度になります。</p>
    <p><strong>◆ メインストーリーを進める（バトル → ストーリー）</strong><br>
    操作手順：下メニューの「バトル」→「ストーリー」→「1章-1」からタップして開始。バトルはオートで進むので見ているだけでOKです（右上の「オート」ボタンをタップするとキャラが自動で戦います）。</p>
    <p><strong>◆ デイリーミッションを確認する</strong><br>
    ホーム画面の「ミッション」または「！」アイコンをタップ。「今日やること」リストが表示されます。達成できたものから報酬を受け取りましょう。<strong>デイリーミッションを毎日こなすと経験値ボーナスがもらえます。</strong></p>
    <p><strong>◆ スタミナが切れたらやめる</strong><br>
    スタミナが0になったら、その日のプレイは終了でOK。回復アイテムは翌日以降のために温存しましょう。</p>
  </div>
</div>

<div class="day-step">
  <div class="day-step__num">2</div>
  <div class="day-step__content">
    <h4>Day 2〜4（各1.5〜2時間）：ランク6〜15</h4>
    <p><strong>◆ 毎日のルーティン（必ず守る3つのこと）</strong></p>
    <ol>
      <li><strong>デイリーログインボーナスを受け取る</strong>：ホーム画面を開くと自動でポップアップが出る。タップして受け取る（所要30秒）</li>
      <li><strong>デイリーミッションをこなす</strong>：ミッション画面を開いて達成できるものからクリア（所要15〜20分）</li>
      <li><strong>スタミナを全て使い切る</strong>：バトル → ストーリーで1章ずつ進める。スタミナが切れたら回復アイテムを使って追加バトル（1〜2回）</li>
    </ol>
    <p><strong>◆ モンスターを強化して戦力アップ</strong><br>
    バトルで詰まったら強化が必要です。操作手順：下メニューの「モンスター」→ 強化したいモンスターを選ぶ →「強化」→「素材を選ぶ」→ バトルで集めた強化素材を使う。<strong>主力として使うモンスター1〜2体に集中して強化する</strong>のが効率的。</p>
    <p><strong>◆ ランク10で新機能が解放される</strong><br>
    ランク10に到達すると「ギルド（同盟）」機能が解放されます。ギルドに入ると毎日ギルドポイントがもらえ、強化素材と交換できます。ランク10になったらすぐにギルドに申請しましょう（ホーム → ギルドアイコン → 「ギルドを探す」→ 人数の多いギルドを選ぶ）。</p>
  </div>
</div>

<div class="day-step">
  <div class="day-step__num">5</div>
  <div class="day-step__content">
    <h4>Day 5〜6（各1.5時間）：ランク16〜19（山場）</h4>
    <p><strong>◆ この段階で詰まりやすいポイント</strong><br>
    ランク15以降はバトルの難易度が上がります。負けてしまう場合は以下を確認してください。</p>
    <ul>
      <li>モンスターのレベルが低い → 強化素材を集めて強化</li>
      <li>モンスターの属性が不利 → バトル → 「弱点」表示を確認して有利属性のモンスターを使う</li>
      <li>チームの組み合わせが悪い → 前衛・後衛・サポートをバランスよく配置</li>
    </ul>
    <p><strong>◆ スタミナ回復アイテムを積極的に使う</strong><br>
    温存していた回復アイテムをここで使いましょう。ホーム → アイテムバッグ（バッグのアイコン）→ 「AP回復薬」を使うと即時回復。残り2〜3日でランク20まであと少しの場合、惜しまず使ってOK。</p>
    <p><strong>◆ 1日のプレイ回数を増やす</strong><br>
    朝・昼・夜の3回に加えて、帰宅後や就寝前にもう1回プレイを追加するとランクアップが早まります。</p>
  </div>
</div>

<div class="day-step day-step--final">
  <div class="day-step__num">7</div>
  <div class="day-step__content">
    <h4>Day 6〜7（1時間）：ランク20達成 🎉</h4>
    <p><strong>◆ ランク20の確認方法</strong><br>
    ホーム画面の上部にあるプレイヤーアイコンをタップ → 「プロフィール」→ 「レベル（ランク）」に「20」と表示されていればOK。</p>
    <p><strong>◆ 達成後の注意点</strong><br>
    ポイントサイトの管理画面で「未確定」として1〜3週間後に反映されます。反映されない場合は、ポイントサイトのサポートに「達成日時・プレイヤーID」を伝えて問い合わせましょう。</p>
  </div>
</div>
</div>

<h2>よくある質問Q&A</h2>
<div class="faq-item"><div class="faq-item__q">バトルに負けてしまって先に進めません</div><div class="faq-item__a">モンスターの強化が不足しています。バトル画面でそのステージの「推奨戦力」を確認し、自分の戦力と比較してください。戦力が低ければ、もう一度前のステージを周回して強化素材を集め、モンスターをレベルアップさせましょう。</div></div>
<div class="faq-item"><div class="faq-item__q">スタミナが回復しているうちにバトルを終わらせたいです</div><div class="faq-item__a">スタミナ5分に1回復なので、例えば出勤前・昼休み・帰宅後・就寝前と4回に分けてプレイすると効率的です。スタミナ上限（60〜80）を溢れさせるのがもったいないので、こまめにゲームを開く習慣をつけましょう。</div></div>
<div class="faq-item"><div class="faq-item__q">課金しないと無理ですか？</div><div class="faq-item__a">ランク20程度は完全無課金で達成できます。ただし、ガチャで強いモンスターを引くのは課金要素です。ポイ活目的なら無課金で問題ありません。</div></div>
<div class="faq-item"><div class="faq-item__q">7日以内に間に合わない気がします</div><div class="faq-item__a">余裕を持って開始することが重要です。案件の期限を確認し、達成期限の7〜10日前にインストールしましょう。万が一間に合わない場合、ポイントサイトによっては期限延長の申請ができる場合もあります。</div></div>

<h2>まとめ：最短達成の4か条</h2>
<ol>
<li><strong>スタミナを1日3〜4回に分けて使い切る</strong>（溜め込まない）</li>
<li><strong>デイリーミッションを毎日こなして経験値ボーナスを受け取る</strong></li>
<li><strong>ランク10でギルドに入ってアイテムをもらう</strong></li>
<li><strong>回復アイテムはランク16以降の山場で惜しまず使う</strong></li>
</ol>
<p>毎日コツコツ続ければ、ゲーム初心者でも7日以内にMoppy最大4,500円を達成できます。</p>
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
    print("モンスターバスケット 詳細版リライト中...")
    patch_article(CONTENT)
    print("完了")
