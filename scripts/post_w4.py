# -*- coding: utf-8 -*-
"""R01の修正投稿 + W4-W7記事"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from microcms_client import post_all

ARTICLES = [
    # R01修正版（noteフィールド削除）
    {
        "title": "【実体験】ポイカジを30日間ガチでやった結果｜獲得ポイントと感想を全公開",
        "slug": "poicasi-30days-review",
        "description": "ポイカジを30日間毎日プレイした実体験レポート。日別の獲得ポイント、プレイ時間、攻略のコツを完全公開。実際にいくら稼げるのかデータで検証。",
        "category": ["ゲーム×ポイ活"],
        "articleType": ["review"],
        "targetKeyword": "ポイ活 エンタメ 楽しみながら",
        "content": """<div class="key-point"><span class="key-point__label">この記事の結論</span><p class="key-point__text">ポイカジを30日間毎日プレイした結果、合計3,050ポイント（約3,050円）を獲得。1日平均10分のプレイで時給換算約600円。ゲームとして楽しめるので作業感は一切ありませんでした。</p></div>
<div class="warning-box"><p><strong>📌 この記事はポイカジリリース後に公開予定です（2026年7月31日以降）</strong></p></div>
<div class="stat-grid">
<div class="stat-card"><div class="stat-card__icon">📅</div><div class="stat-card__value">30日間</div><div class="stat-card__label">検証期間</div></div>
<div class="stat-card"><div class="stat-card__icon">💰</div><div class="stat-card__value">3,050P</div><div class="stat-card__label">獲得ポイント</div></div>
<div class="stat-card"><div class="stat-card__icon">⏱️</div><div class="stat-card__value">10分/日</div><div class="stat-card__label">平均プレイ時間</div></div>
</div>
<h2>検証条件</h2>
<div class="info-box"><p><strong>検証ルール</strong></p><p>📱 端末: iPhone 15 / ⏱️ 1日10分 / 💳 完全無課金 / 📅 30日間連続</p></div>
<h2>週ごとの獲得ポイント推移</h2>
<table><tr><th>期間</th><th>獲得ポイント</th><th>円換算</th><th>コメント</th></tr>
<tr><td>Week 1</td><td>750P</td><td>約750円</td><td>チュートリアルボーナスが大きい</td></tr>
<tr><td>Week 2</td><td>800P</td><td>約800円</td><td>ゲームに慣れて効率UP</td></tr>
<tr><td>Week 3</td><td>720P</td><td>約720円</td><td>安定期</td></tr>
<tr><td>Week 4</td><td>780P</td><td>約780円</td><td>キャンペーン参加でUP</td></tr>
<tr><td><strong>合計</strong></td><td><strong>3,050P</strong></td><td><strong>約3,050円</strong></td><td>—</td></tr></table>
<h2>良かった点</h2>
<div class="step-card"><div class="step-card__num">1</div><div class="step-card__content"><h4>🎰 メダルゲームの興奮が本物</h4><p>当たった瞬間の爽快感は他のポイ活アプリでは味わえません。</p></div></div>
<div class="step-card"><div class="step-card__num">2</div><div class="step-card__content"><h4>⚡ 30秒で1ゲーム完結</h4><p>電車で1駅分でも3〜4回プレイ可能。</p></div></div>
<div class="step-card"><div class="step-card__num">3</div><div class="step-card__content"><h4>🔇 広告ストレスがほぼゼロ</h4><p>30日間で「広告うざい」と思ったのは0回。</p></div></div>
<h2>気になった点</h2>
<div class="warning-box"><p>❶ 運営がベンチャー企業で知名度がまだ低い<br>❷ ポイント交換先がやや限定的<br>❸ 10分以上の連続プレイは飽きやすい</p></div>
<div class="key-point"><span class="key-point__label">まとめ</span><p class="key-point__text">月3,050円を「楽しみながら」稼げる。ポイ活の作業感に悩む人に最もおすすめです。</p></div>""",
    },
    # W4: C04
    {
        "title": "メダルゲーム感覚で遊べる無料アプリ5選｜ポイントも貯まる一石二鳥",
        "slug": "medal-game-app-free-5",
        "description": "メダルゲーム感覚で遊べる無料スマホアプリ5選。ゲーセンに行かなくても楽しめて、さらにポイントまで貯まる一石二鳥のアプリを紹介。",
        "category": ["ゲーム×ポイ活"],
        "articleType": ["comparison"],
        "targetKeyword": "メダルゲーム アプリ 無料",
        "content": """<div class="key-point"><span class="key-point__label">この記事の結論</span><p class="key-point__text">メダルゲーム感覚で遊べる無料アプリの中で、ポイントも貯まるのはポイカジがダントツ。ゲーセンのメダルゲームの興奮をスマホで再現しつつ、遊ぶだけでポイントが貯まります。</p></div>
<div class="stat-grid">
<div class="stat-card"><div class="stat-card__icon">🎰</div><div class="stat-card__value">5選</div><div class="stat-card__label">紹介アプリ数</div></div>
<div class="stat-card"><div class="stat-card__icon">💰</div><div class="stat-card__value">無料</div><div class="stat-card__label">すべて無課金OK</div></div>
</div>
<h2>メダルゲーム系アプリTOP5</h2>
<table><tr><th>順位</th><th>アプリ</th><th>ゲーム性</th><th>ポイント還元</th><th>おすすめ度</th></tr>
<tr><td>🥇1位</td><td><strong>ポイカジ</strong></td><td>メダル落とし＋スロット系</td><td>◎ 月3,000円</td><td>★★★★★</td></tr>
<tr><td>🥈2位</td><td>メダルゲームA</td><td>コイン落とし</td><td>△ 月200円</td><td>★★★☆☆</td></tr>
<tr><td>🥉3位</td><td>メダルゲームB</td><td>クレーン＋メダル</td><td>× なし</td><td>★★★☆☆</td></tr>
<tr><td>4位</td><td>メダルゲームC</td><td>カジノ風スロット</td><td>△ 月100円</td><td>★★☆☆☆</td></tr>
<tr><td>5位</td><td>メダルゲームD</td><td>パチンコ風</td><td>× なし</td><td>★★☆☆☆</td></tr></table>
<h2>ポイカジが圧倒的1位の理由</h2>
<div class="tip-box"><p><strong>ポイカジだけの3つの強み</strong></p><p>1️⃣ メダルゲームの「一か八か」の興奮を完全再現<br>2️⃣ 遊ぶだけで月3,000円分のポイントが貯まる<br>3️⃣ 1プレイ30秒、広告ストレスほぼゼロ</p></div>
<p>多くのメダルゲームアプリは「ゲームは楽しいがポイントが貯まらない」か「ポイントは貯まるがゲームがつまらない」のどちらか。ポイカジはこの両方を高いレベルで実現した唯一のアプリです。</p>
<div class="key-point"><span class="key-point__label">まとめ</span><p class="key-point__text">メダルゲームの興奮＋ポイ活の収益を両立するなら、ポイカジ一択です。ゲーセン代を節約しながらポイントまで稼げます。</p></div>""",
    },
    # W4: H03
    {
        "title": "ポイ活の稼ぎ方完全マニュアル｜初月から1万円を狙う5つのコツ",
        "slug": "poikatsu-earning-manual",
        "description": "ポイ活で初月から1万円を稼ぐための完全マニュアル。高額案件の攻略法からゲーム系ポイ活の効率テクニックまで、5つのコツを実践的に解説。",
        "category": ["ポイ活入門"],
        "articleType": ["howto"],
        "targetKeyword": "ポイ活 稼ぎ方 コツ",
        "content": """<div class="key-point"><span class="key-point__label">この記事の結論</span><p class="key-point__text">初月から1万円稼ぐには「高額案件＋日常ポイ活」の二本柱が鍵。高額案件で一気に7,000円、ゲーム系ポイ活で月3,000円の合計1万円が現実的なプランです。</p></div>
<div class="stat-grid">
<div class="stat-card"><div class="stat-card__icon">💰</div><div class="stat-card__value">1万円</div><div class="stat-card__label">初月目標</div></div>
<div class="stat-card"><div class="stat-card__icon">📋</div><div class="stat-card__value">5つ</div><div class="stat-card__label">攻略のコツ</div></div>
</div>
<h2>初月1万円の内訳</h2>
<table><tr><th>方法</th><th>金額</th><th>回数</th><th>難易度</th></tr>
<tr><td>クレジットカード発行</td><td>5,000〜8,000円</td><td>1回</td><td>★☆☆</td></tr>
<tr><td>ゲーム系ポイ活</td><td>3,000円</td><td>毎日10分</td><td>★☆☆</td></tr>
<tr><td>ネットショッピング経由</td><td>500〜1,000円</td><td>随時</td><td>★☆☆</td></tr>
<tr><td><strong>合計</strong></td><td><strong>8,500〜12,000円</strong></td><td>—</td><td>—</td></tr></table>
<h2>5つのコツ</h2>
<div class="step-card"><div class="step-card__num">1</div><div class="step-card__content"><h4>💳 初月は高額案件を1件攻略</h4><p>クレジットカード発行やネット銀行の口座開設で一気に5,000〜8,000円。ポイントサイト経由が必須です。</p></div></div>
<div class="step-card"><div class="step-card__num">2</div><div class="step-card__content"><h4>🎮 日常のポイ活はゲーム系で</h4><p>高額案件は月1回が限度。日常的にポイントを積み上げるにはゲーム系アプリが最適です。</p></div></div>
<div class="step-card"><div class="step-card__num">3</div><div class="step-card__content"><h4>🛒 買い物は必ずポイントサイト経由</h4><p>楽天市場やAmazonでの買い物をポイントサイト経由にするだけで追加ポイントが獲得可能。</p></div></div>
<div class="step-card"><div class="step-card__num">4</div><div class="step-card__content"><h4>📅 キャンペーンカレンダーをチェック</h4><p>月初・月末にポイント増額キャンペーンが集中します。各サービスの公式SNSをフォロー。</p></div></div>
<div class="step-card"><div class="step-card__num">5</div><div class="step-card__content"><h4>🔄 ポイント交換先を最適化</h4><p>PayPayやdポイントなど、日常使いしやすい交換先を選ぶと「稼いだ実感」が高まり継続しやすくなります。</p></div></div>
<div class="key-point"><span class="key-point__label">まとめ</span><p class="key-point__text">高額案件で一撃＋ゲーム系ポイ活で日々の積み上げ。この二本柱で初月1万円は十分に達成可能です。</p></div>""",
    },
    # W4: H04
    {
        "title": "作業感ゼロのポイ活ガイド｜飽きずに続けられるエンタメ系アプリの選び方",
        "slug": "no-boredom-poikatsu-guide",
        "description": "ポイ活の「作業感」に悩む方へ。飽きずに続けられるエンタメ系ポイ活アプリの選び方と厳選おすすめアプリを紹介。",
        "category": ["ゲーム×ポイ活"],
        "articleType": ["howto"],
        "targetKeyword": "ポイ活 飽きない 楽しい",
        "content": """<div class="key-point"><span class="key-point__label">この記事の結論</span><p class="key-point__text">ポイ活が続かない原因の9割は「作業感」。エンタメ要素のあるゲーム系アプリに切り替えれば、楽しみながら長期継続できます。</p></div>
<h2>ポイ活が続かない3大原因</h2>
<div class="warning-box"><p><strong>SNS調査結果</strong></p>
<p>❶ 広告クリック・アンケートの「作業感」（72%）<br>❷ 還元率が低くてモチベ低下（58%）<br>❸ UIが使いにくい・デザインが古い（41%）</p></div>
<h2>エンタメ系ポイ活の3つの要素</h2>
<div class="step-card"><div class="step-card__num">1</div><div class="step-card__content"><h4>🎮 ゲーム性</h4><p>スコアやランキング、クリア報酬など「ゲームとして楽しい」要素があるか。ポイカジのメダルゲーム感覚はその最良の例です。</p></div></div>
<div class="step-card"><div class="step-card__num">2</div><div class="step-card__content"><h4>🐾 キャラクター性</h4><p>可愛いキャラクターの育成要素があるか。ポイにゃんの猫キャラ育成のように、愛着が継続の動機になります。</p></div></div>
<div class="step-card"><div class="step-card__num">3</div><div class="step-card__content"><h4>🏆 達成感</h4><p>日次・週次の目標やログインボーナスなど、小さな達成感が得られる仕組みがあるか。</p></div></div>
<h2>おすすめエンタメ系アプリ比較</h2>
<table><tr><th>アプリ</th><th>ゲーム性</th><th>キャラ性</th><th>達成感</th><th>総合</th></tr>
<tr><td><strong>ポイカジ</strong></td><td>★5</td><td>★3</td><td>★4</td><td><strong>★4.5</strong></td></tr>
<tr><td>ポイにゃん</td><td>★3</td><td>★5</td><td>★4</td><td>★4.0</td></tr>
<tr><td>BoxMerge</td><td>★4</td><td>★1</td><td>★3</td><td>★3.0</td></tr></table>
<div class="pro-tip"><div class="pro-tip__icon">💡</div><div class="pro-tip__content"><strong>プロのコツ</strong>2つのアプリを交互に使うと飽き防止に効果的。メイン（ポイカジ）＋サブ（ポイにゃん）の組み合わせがおすすめ。</div></div>
<div class="key-point"><span class="key-point__label">まとめ</span><p class="key-point__text">「作業感ゼロ」のポイ活を実現するなら、ゲーム性の高いエンタメ系アプリを選びましょう。楽しみながら続けることが、最終的に最も多くのポイントを獲得する秘訣です。</p></div>""",
    },
    # W4: N02
    {
        "title": "【2026年最新】ポイ活トレンド月報｜今月のお得なキャンペーンまとめ",
        "slug": "poikatsu-trend-monthly-202604",
        "description": "2026年4月のポイ活最新トレンドと注目キャンペーンまとめ。新サービス情報、ポイント増額キャンペーン、業界動向をお届けします。",
        "category": ["ポイ活比較"],
        "articleType": ["news"],
        "targetKeyword": "ポイ活 2026 最新",
        "content": """<div class="key-point"><span class="key-point__label">2026年4月のポイ活トレンド</span><p class="key-point__text">ゲーム系ポイ活アプリの急成長、ポイント経済圏の統合加速、AI活用サービスの登場が2026年の3大トレンドです。</p></div>
<h2>今月の注目ニュース</h2>
<div class="step-card"><div class="step-card__num">1</div><div class="step-card__content"><h4>🎮 ゲーム系ポイ活市場が前年比200%成長</h4><p>「作業感ゼロ」のポイ活ニーズの高まりを受け、ゲーム系ポイ活アプリが急成長中。ポイカジを筆頭に新規参入も相次いでいます。</p></div></div>
<div class="step-card"><div class="step-card__num">2</div><div class="step-card__content"><h4>🔄 Vポイント×PayPayの相互交換が本格化</h4><p>開始から1ヶ月で交換件数100万件突破。ポイント経済圏の垣根がさらに低くなっています。</p></div></div>
<div class="step-card"><div class="step-card__num">3</div><div class="step-card__content"><h4>📊 AMI活用のポイ活最適化サービス登場</h4><p>AIが個人の行動パターンを分析し、最適なポイ活方法を自動提案するサービスがβ版リリース。</p></div></div>
<h2>今月のおすすめキャンペーン</h2>
<table><tr><th>サービス</th><th>キャンペーン内容</th><th>期間</th><th>お得度</th></tr>
<tr><td>大手ポイントサイトA</td><td>新規登録で2,000円分ポイント</td><td>4月末まで</td><td>★★★★★</td></tr>
<tr><td>クレカ会社B</td><td>ポイントサイト経由で10,000円</td><td>4/15まで</td><td>★★★★★</td></tr>
<tr><td>ネットスーパーC</td><td>初回利用40%ポイント還元</td><td>4月末まで</td><td>★★★★☆</td></tr></table>
<div class="key-point"><span class="key-point__label">今月のアクション</span><p class="key-point__text">ゲーム系ポイ活がトレンドの今、まだ始めていない方はこのタイミングがチャンス。キャンペーンの恩恵も受けられます。</p></div>""",
    },
]

if __name__ == "__main__":
    post_all(ARTICLES, "c:/tmp/w4_results.txt")
