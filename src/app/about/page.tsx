import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'ポイ活ラボとは | ポイ活ラボ by ポイカジ',
  description: 'ポイ活ラボは「ゲームで稼ぐ、新しいポイ活」をテーマに、時給効率の高いゲーム案件攻略・比較情報を発信するメディアです。',
};

export default function AboutPage() {
  return (
    <main className="static-page">
      <div className="container">
        <nav className="breadcrumb" aria-label="パンくずリスト">
          <a href="/">ホーム</a>
          <span className="breadcrumb__sep" />
          <span>ポイ活ラボとは</span>
        </nav>
        <article className="static-page__content">
          <h1>ポイ活ラボとは</h1>
          <p>
            <strong>ポイ活ラボ by ポイカジ</strong>は、「ゲームで稼ぐ、新しいポイ活」をコンセプトに、
            時給効率の高いゲーム案件の攻略情報・比較・最新ニュースを発信する
            カジュアルゲーム×ポイ活専門メディアです。
          </p>
          <h2>メディアの特徴</h2>
          <ul>
            <li><strong>時給効率で厳選：</strong>報酬÷プレイ時間で算出した「時給効率」が高い案件のみを掲載</li>
            <li><strong>初心者フレンドリー：</strong>操作レベルの手順解説・スタミナ管理・Q&Aで、初めての方でも迷わず達成</li>
            <li><strong>7日以内・5,000円未満：</strong>達成しやすい条件の案件に絞って紹介</li>
          </ul>
          <h2>運営について</h2>
          <p>
            本メディアはポイカジ（2026年7月リリース予定のカジュアルゲーム型ポイ活アプリ）が運営しています。
            リリース前から、既存のゲームポイ活情報をお届けしています。
          </p>
          <div className="static-page__cta">
            <a href="/category/game-guide" className="poicasi-coming-soon__btn poicasi-coming-soon__btn--primary">
              🎮 ゲーム攻略記事を見る
            </a>
          </div>
        </article>
      </div>
    </main>
  );
}
