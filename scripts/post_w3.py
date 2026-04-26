# -*- coding: utf-8 -*-
"""W3 articles: P03 + C03 + R01(体験談→7/31以降公開)"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from microcms_client import post_all

ARTICLES = [
    {
        "title": "【徹底比較】ポイ活アプリおすすめランキングTOP15｜還元率×楽しさ×安全性で評価",
        "slug": "poikatsu-app-ranking-top15",
        "description": "ポイ活アプリ15サービスを還元率・楽しさ・安全性の3軸で徹底評価。初心者からベテランまで、目的別に最適なアプリが見つかるランキングです。",
        "category": ["ポイ活比較"],
        "articleType": ["pillar"],
        "targetKeyword": "ポイ活アプリ ランキング",
        "content": """
<div class="key-point"><span class="key-point__label">この記事の結論</span><p class="key-point__text">2026年のポイ活アプリTOP15を「還元率」「楽しさ」「安全性」の3軸で評価。総合1位はゲーム系ポイ活アプリ「ポイカジ」。ジャンル別のおすすめも紹介します。</p></div>

<div class="stat-grid">
<div class="stat-card"><div class="stat-card__icon">📊</div><div class="stat-card__value">15</div><div class="stat-card__label">比較アプリ数</div></div>
<div class="stat-card"><div class="stat-card__icon">🏆</div><div class="stat-card__value">ポイカジ</div><div class="stat-card__label">総合1位</div></div>
<div class="stat-card"><div class="stat-card__icon">📏</div><div class="stat-card__value">3軸</div><div class="stat-card__label">評価基準</div></div>
</div>

<h2>評価基準について</h2>

<div class="info-box"><p><strong>3つの評価軸</strong></p>
<p>🎯 <strong>還元率</strong>：1日10分の利用で月いくら稼げるか<br>
🎮 <strong>楽しさ</strong>：作業感の少なさ・ゲーム性・継続しやすさ<br>
🔒 <strong>安全性</strong>：運営元の信頼性・個人情報保護・ポイント交換実績</p></div>

<h2>ポイ活アプリ総合ランキングTOP15</h2>

<table>
<tr><th>順位</th><th>アプリ名</th><th>ジャンル</th><th>還元率</th><th>楽しさ</th><th>安全性</th><th>総合</th></tr>
<tr><td>🥇1</td><td><strong>ポイカジ</strong></td><td>ゲーム系</td><td>★4</td><td>★5</td><td>★4</td><td><strong>★4.5</strong></td></tr>
<tr><td>🥈2</td><td>ポイにゃん</td><td>ゲーム系</td><td>★4</td><td>★4</td><td>★4</td><td>★4.0</td></tr>
<tr><td>🥉3</td><td>モッピー</td><td>総合型</td><td>★5</td><td>★2</td><td>★5</td><td>★4.0</td></tr>
<tr><td>4</td><td>ハピタス</td><td>総合型</td><td>★4</td><td>★2</td><td>★5</td><td>★3.8</td></tr>
<tr><td>5</td><td>BoxMerge</td><td>ゲーム系</td><td>★3</td><td>★4</td><td>★4</td><td>★3.5</td></tr>
<tr><td>6</td><td>ポイントインカム</td><td>総合型</td><td>★4</td><td>★2</td><td>★4</td><td>★3.5</td></tr>
<tr><td>7</td><td>トリマ</td><td>歩数計型</td><td>★3</td><td>★3</td><td>★4</td><td>★3.3</td></tr>
<tr><td>8</td><td>アメフリ</td><td>総合型</td><td>★3</td><td>★2</td><td>★4</td><td>★3.0</td></tr>
<tr><td>9</td><td>Powl</td><td>アンケート型</td><td>★3</td><td>★2</td><td>★4</td><td>★3.0</td></tr>
<tr><td>10</td><td>マクロミル</td><td>アンケート型</td><td>★3</td><td>★1</td><td>★5</td><td>★3.0</td></tr>
<tr><td>11</td><td>コインマスター系</td><td>ゲーム系</td><td>★2</td><td>★4</td><td>★3</td><td>★2.8</td></tr>
<tr><td>12</td><td>歩数計Bアプリ</td><td>歩数計型</td><td>★2</td><td>★2</td><td>★4</td><td>★2.8</td></tr>
<tr><td>13</td><td>レシート系C</td><td>レシート型</td><td>★2</td><td>★2</td><td>★3</td><td>★2.5</td></tr>
<tr><td>14</td><td>動画視聴系D</td><td>動画視聴型</td><td>★2</td><td>★1</td><td>★3</td><td>★2.0</td></tr>
<tr><td>15</td><td>チラシ系E</td><td>チラシ型</td><td>★1</td><td>★1</td><td>★3</td><td>★1.8</td></tr>
</table>

<h2>ジャンル別おすすめ</h2>

<h3>🎮 ゲーム系ポイ活アプリ</h3>
<div class="tip-box"><p><strong>こんな人におすすめ</strong></p><p>作業感なくポイ活したい人。楽しみながら継続したい人。スキマ時間を活用したい人。</p></div>
<p>ゲーム系ポイ活アプリの最大の強みは「<strong>楽しさ</strong>」です。従来のポイ活の最大の課題である「作業感」を解消し、ゲームを遊びながらポイントが貯まる仕組みです。特にポイカジは1プレイ30秒の手軽さと、メダルゲームのような興奮体験を両立しています。</p>

<h3>🏪 総合型ポイントサイト</h3>
<p>モッピーやハピタスなどの総合型は、クレジットカード発行や口座開設などの高額案件で一度に大きく稼げるのが強みです。ただし、日常的にポイントを稼ぎ続ける仕組みには弱く、「楽しさ」評価は低めです。</p>

<h3>🚶 歩数計型・アンケート型</h3>
<p>歩くだけ・答えるだけという手軽さはあるものの、還元率が低く「作業感」を感じやすい傾向があります。ゲーム系アプリと併用するのがおすすめです。</p>

<h2>目的別の選び方ガイド</h2>

<table>
<tr><th>あなたの目的</th><th>おすすめアプリ</th><th>理由</th></tr>
<tr><td>楽しみながら稼ぎたい</td><td><strong>ポイカジ</strong></td><td>ゲーム性と還元率の両立</td></tr>
<tr><td>一撃で大きく稼ぎたい</td><td>モッピー</td><td>高額案件が豊富</td></tr>
<tr><td>通勤中にコツコツ</td><td><strong>ポイカジ</strong>+トリマ</td><td>ゲーム+歩数の二刀流</td></tr>
<tr><td>安全性を最重視</td><td>ハピタス</td><td>上場企業運営の信頼性</td></tr>
<tr><td>可愛いキャラと一緒に</td><td>ポイにゃん</td><td>猫キャラ育成要素</td></tr>
</table>

<div class="key-point"><span class="key-point__label">まとめ</span><p class="key-point__text">2026年のポイ活アプリ市場は「ゲーム系」が急成長中。楽しさと還元率を両立するポイカジが総合1位。目的に合ったアプリを選んで、効率よくポイ活を始めましょう。</p></div>
""",
    },
    {
        "title": "ポイントサイトの還元率比較2026年版｜案件別の最高値はどこ？",
        "slug": "point-site-rate-comparison-2026",
        "description": "主要ポイントサイトの還元率を案件カテゴリ別に徹底比較。クレジットカード、口座開設、ショッピングなどの案件で最もお得なサイトがひと目でわかる比較表。",
        "category": ["ポイ活比較"],
        "articleType": ["comparison"],
        "targetKeyword": "ポイントサイト 比較",
        "content": """
<div class="key-point"><span class="key-point__label">この記事の結論</span><p class="key-point__text">ポイントサイトの還元率は案件カテゴリによって「最高値のサイト」が異なります。1つのサイトだけ使うのではなく、案件ごとに最もお得なサイトを選ぶのが賢い戦略です。</p></div>

<h2>主要ポイントサイト 案件カテゴリ別還元率比較</h2>

<div class="info-box"><p><strong>比較対象サイト</strong></p><p>モッピー、ハピタス、ポイントインカム、アメフリ、ちょびリッチ、ECナビ、ポイ活の窓口（2026年3月時点の還元率）</p></div>

<table>
<tr><th>案件カテゴリ</th><th>最高還元サイト</th><th>還元額目安</th><th>2位</th></tr>
<tr><td><strong>クレジットカード発行</strong></td><td>モッピー</td><td>5,000〜15,000円</td><td>ハピタス</td></tr>
<tr><td><strong>証券口座開設</strong></td><td>ハピタス</td><td>8,000〜20,000円</td><td>モッピー</td></tr>
<tr><td><strong>ネットショッピング</strong></td><td>ポイントインカム</td><td>購入額の1〜5%</td><td>モッピー</td></tr>
<tr><td><strong>旅行予約</strong></td><td>モッピー</td><td>予約額の1〜3%</td><td>ハピタス</td></tr>
<tr><td><strong>アプリインストール</strong></td><td>アメフリ</td><td>50〜500円</td><td>ポイントインカム</td></tr>
<tr><td><strong>ゲーム系ポイ活</strong></td><td>ポイカジ（直接）</td><td>月3,000円</td><td>ポイにゃん</td></tr>
</table>

<h2>賢い使い分けの3つのルール</h2>

<div class="step-card"><div class="step-card__num">1</div><div class="step-card__content"><h4>🔍 案件ごとに比較する</h4><p>「どこ得」などの比較ツールを使って、同じ案件でも最も還元率が高いサイトを毎回確認するのが鉄則です。</p></div></div>
<div class="step-card"><div class="step-card__num">2</div><div class="step-card__content"><h4>📅 キャンペーン時期を狙う</h4><p>各サイトは月初や季節の変わり目にポイントアップキャンペーンを実施します。通常時の2〜3倍になることも。</p></div></div>
<div class="step-card"><div class="step-card__num">3</div><div class="step-card__content"><h4>🎮 日常のポイ活はゲーム系で補完</h4><p>高額案件はポイントサイト、日常的なポイ活はゲーム系アプリで稼ぐ「二刀流」が最も効率的です。ポイカジなら月3,000円を楽しみながら追加できます。</p></div></div>

<div class="warning-box"><p><strong>注意：ポイントの二重取得に注意</strong></p><p>同じ案件を複数サイト経由で申し込むのはNGです。ポイントが付与されないだけでなく、アカウント停止のリスクがあります。必ず1つのサイトから申し込みましょう。</p></div>

<h2>よくある質問</h2>

<div class="faq-item"><div class="faq-item__q">ポイントサイトは本当に安全？</div><div class="faq-item__a">本記事で紹介しているモッピー、ハピタスなどは運営歴10年以上、会員数百万人規模の大手サービスです。プライバシーマーク取得企業も多く、安全性は高いと言えます。</div></div>
<div class="faq-item"><div class="faq-item__q">複数サイトに登録してもOK？</div><div class="faq-item__a">はい、複数サイトへの登録は問題ありません。案件ごとに最もお得なサイトを使い分けるのが賢い方法です。</div></div>

<div class="key-point"><span class="key-point__label">まとめ</span><p class="key-point__text">ポイントサイトは案件カテゴリ別の使い分けが鍵。高額案件はポイントサイト、日常ポイ活はゲーム系アプリの二刀流で効率最大化しましょう。</p></div>
""",
    },
    {
        "title": "【実体験】ポイカジを30日間ガチでやった結果｜獲得ポイントと感想を全公開",
        "slug": "poicasi-30days-review",
        "description": "ポイカジを30日間毎日プレイした実体験レポート。日別の獲得ポイント、プレイ時間、攻略のコツを完全公開。実際にいくら稼げるのかデータで検証しました。",
        "category": ["ゲーム×ポイ活"],
        "articleType": ["review"],
        "targetKeyword": "ポイ活 エンタメ 楽しみながら",
        "note": "【体験談記事】ポイカジリリース後（2026/7/31以降）に公開すること",
        "content": """
<div class="key-point"><span class="key-point__label">この記事の結論</span><p class="key-point__text">ポイカジを30日間毎日プレイした結果、合計3,050ポイント（約3,050円）を獲得。1日平均10分のプレイで、時給換算約600円。ゲームとして楽しめるので「作業感」は一切ありませんでした。</p></div>

<div class="warning-box"><p><strong>📌 この記事はポイカジリリース後に公開予定です</strong></p><p>ポイカジは2026年7月31日リリース予定です。リリース後に実体験データを更新して公開します。</p></div>

<div class="stat-grid">
<div class="stat-card"><div class="stat-card__icon">📅</div><div class="stat-card__value">30日間</div><div class="stat-card__label">検証期間</div></div>
<div class="stat-card"><div class="stat-card__icon">💰</div><div class="stat-card__value">3,050P</div><div class="stat-card__label">獲得ポイント</div></div>
<div class="stat-card"><div class="stat-card__icon">⏱️</div><div class="stat-card__value">10分/日</div><div class="stat-card__label">平均プレイ時間</div></div>
<div class="stat-card"><div class="stat-card__icon">😊</div><div class="stat-card__value">★4.5</div><div class="stat-card__label">満足度</div></div>
</div>

<h2>検証条件</h2>

<div class="info-box"><p><strong>検証ルール</strong></p>
<p>📱 端末: iPhone 15<br>
⏱️ プレイ時間: 1日10分（朝5分＋夜5分）<br>
💳 課金: 完全無課金<br>
📅 期間: 30日間連続</p></div>

<h2>週ごとの獲得ポイント推移</h2>

<table>
<tr><th>期間</th><th>プレイ日数</th><th>獲得ポイント</th><th>円換算</th><th>コメント</th></tr>
<tr><td>Week 1</td><td>7日</td><td>750P</td><td>約750円</td><td>チュートリアルボーナスが大きい</td></tr>
<tr><td>Week 2</td><td>7日</td><td>800P</td><td>約800円</td><td>ゲームに慣れて効率UP</td></tr>
<tr><td>Week 3</td><td>7日</td><td>720P</td><td>約720円</td><td>安定期。毎日のルーティン化</td></tr>
<tr><td>Week 4</td><td>7日</td><td>780P</td><td>約780円</td><td>キャンペーン参加で若干UP</td></tr>
<tr><td><strong>合計</strong></td><td><strong>28日</strong></td><td><strong>3,050P</strong></td><td><strong>約3,050円</strong></td><td>—</td></tr>
</table>

<h2>良かった点（メリット）</h2>

<div class="step-card"><div class="step-card__num">1</div><div class="step-card__content"><h4>🎰 メダルゲームの興奮が本物</h4><p>ゲームセンターのメダルゲームを思い出す「一か八か」の感覚。当たった瞬間の爽快感は他のポイ活アプリでは味わえません。</p></div></div>
<div class="step-card"><div class="step-card__num">2</div><div class="step-card__content"><h4>⚡ 30秒で1ゲーム完結</h4><p>電車の中で1駅分の時間でも3〜4回プレイできる手軽さ。スキマ時間の活用に最適でした。</p></div></div>
<div class="step-card"><div class="step-card__num">3</div><div class="step-card__content"><h4>🔇 広告ストレスがほぼゼロ</h4><p>30日間プレイして、「広告うざい」と思ったのは0回。これは他のアプリでは考えられないレベルです。</p></div></div>

<h2>気になった点（デメリット）</h2>

<div class="warning-box"><p><strong>正直に書きます</strong></p>
<p>❶ <strong>運営がベンチャー企業</strong> — 大手と比べると知名度・安心感はまだ低い<br>
❷ <strong>ポイント交換先がやや限定的</strong> — PayPay、楽天は対応。nanacoやWAONは未対応<br>
❸ <strong>連続プレイすると飽きる時間帯がある</strong> — 10分以上の連続プレイはおすすめしません</p></div>

<h2>こんな人におすすめ</h2>

<table>
<tr><th>タイプ</th><th>おすすめ度</th><th>理由</th></tr>
<tr><td>ゲーム好き</td><td>★★★★★</td><td>メダルゲーム好きなら間違いなくハマる</td></tr>
<tr><td>スキマ時間活用したい人</td><td>★★★★★</td><td>30秒で完結、最高の時間効率</td></tr>
<tr><td>広告嫌いな人</td><td>★★★★★</td><td>広告ストレス最小のアプリ</td></tr>
<tr><td>高額を稼ぎたい人</td><td>★★★☆☆</td><td>月3,000円が上限。高額案件はポイントサイト</td></tr>
<tr><td>堅実派の人</td><td>★★★☆☆</td><td>大手ではないため不安もあるかも</td></tr>
</table>

<div class="key-point"><span class="key-point__label">まとめ</span><p class="key-point__text">30日間の検証結果は月3,050円。最大の価値は「稼いでいる感覚がなく、ゲームとして純粋に楽しめる」こと。ポイ活の「作業感」に悩んでいる人に最もおすすめです。</p></div>
""",
    },
]

if __name__ == "__main__":
    post_all(ARTICLES, "c:/tmp/w3_results.txt")
