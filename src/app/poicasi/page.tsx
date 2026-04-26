import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'ポイカジ — 2026年7月リリース予定 | ポイ活ラボ',
  description:
    'ポイカジは毎日30秒で遊べるカジュアルゲームで楽しくポイントを貯めるアプリです。2026年7月のリリースに向け、現在鋭意開発中です。',
};

export default function PoicasiComingSoonPage() {
  return (
    <main className="poicasi-coming-soon">
      {/* Stars bg */}
      <div className="poicasi-coming-soon__stars" aria-hidden="true">
        {Array.from({ length: 60 }).map((_, i) => (
          <span
            key={i}
            className="star"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
              animationDelay: `${(Math.random() * 3).toFixed(2)}s`,
              width: `${Math.random() * 3 + 1}px`,
              height: `${Math.random() * 3 + 1}px`,
            }}
          />
        ))}
      </div>

      <div className="poicasi-coming-soon__inner">
        {/* Logo / Brand */}
        <div className="poicasi-coming-soon__logo">
          <span className="poicasi-coming-soon__logo-icon">🎰</span>
          <span className="poicasi-coming-soon__logo-text">ポイカジ</span>
        </div>

        {/* Heading */}
        <h1 className="poicasi-coming-soon__title">
          もうすぐ<br />
          <em>ゲームしながら</em><br />
          稼げる時代がくる
        </h1>

        <p className="poicasi-coming-soon__desc">
          ポイカジは「30秒で遊べる・毎日続けられる」をコンセプトにした<br className="pc-only" />
          カジュアルゲーム型ポイ活アプリです。<br />
          ゲームを楽しむだけでポイントが貯まる新感覚の体験をお届けします。
        </p>

        {/* Release badge */}
        <div className="poicasi-coming-soon__badge">
          <span className="poicasi-coming-soon__badge-icon">📅</span>
          <div>
            <div className="poicasi-coming-soon__badge-label">リリース予定</div>
            <div className="poicasi-coming-soon__badge-date">2026年7月</div>
          </div>
        </div>

        {/* Features */}
        <div className="poicasi-coming-soon__features">
          <div className="poicasi-feature">
            <span className="poicasi-feature__icon">⚡</span>
            <span className="poicasi-feature__text">1日30秒から<br />始められる</span>
          </div>
          <div className="poicasi-feature">
            <span className="poicasi-feature__icon">🎮</span>
            <span className="poicasi-feature__text">本格カジュアル<br />ゲーム体験</span>
          </div>
          <div className="poicasi-feature">
            <span className="poicasi-feature__icon">💰</span>
            <span className="poicasi-feature__text">毎日遊んで<br />ポイントGET</span>
          </div>
          <div className="poicasi-feature">
            <span className="poicasi-feature__icon">🆓</span>
            <span className="poicasi-feature__text">完全無料<br />課金不要</span>
          </div>
        </div>

        {/* CTA */}
        <div className="poicasi-coming-soon__cta-group">
          <a href="/" className="poicasi-coming-soon__btn poicasi-coming-soon__btn--secondary">
            ← 攻略記事を読む
          </a>
          <a
            href="/category/game-guide"
            className="poicasi-coming-soon__btn poicasi-coming-soon__btn--primary"
          >
            🎮 ゲームでポイ活を始める
          </a>
        </div>

        <p className="poicasi-coming-soon__note">
          リリースまでの間は、ゲームアプリのポイ活（ポイントサイト経由）で<br />
          今すぐ稼ぐことができます。ゲーム攻略記事も充実しています。
        </p>
      </div>
    </main>
  );
}
