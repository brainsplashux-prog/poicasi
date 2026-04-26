import Link from 'next/link';
import { getArticles, getArticlesByCategory, type Article } from '@/lib/microcms';
import ArticleCard from '@/components/ArticleCard';

export const revalidate = 60; // ISR: 60秒ごとに再検証

export default async function Home() {
  let articles: Article[] = [];
  let gameGuideArticles: Article[] = [];
  try {
    const data = await getArticles({ limit: 6 });
    articles = data.contents;
    const gameData = await getArticlesByCategory('ゲーム攻略', 6);
    gameGuideArticles = gameData.contents;
  } catch {
    // microCMS未設定時はダミーデータなしで表示
  }

  return (
    <>
      {/* Hero — Warm Ivory × Gold (Design System HP) */}
      <section className="hero">
        {/* Floating Particles */}
        <div className="hero__particle" aria-hidden="true" />
        <div className="hero__particle" aria-hidden="true" />
        <div className="hero__particle" aria-hidden="true" />
        <div className="hero__particle" aria-hidden="true" />
        <div className="hero__particle" aria-hidden="true" />
        <div className="hero__particle" aria-hidden="true" />
        <div className="hero__inner">
          <span className="hero__badge">⚡ 時給効率特化 ゲームポイ活メディア</span>
          <h1 className="hero__title">
            7日以内・高時給で稼ぐ、<br />
            <span className="hero__title-accent">ゲームポイ活</span>攻略。
          </h1>
          <p className="hero__desc">
            「報酬 ÷ 時間」で計算した時給効率が高いゲームだけを厳選掲載。<br />
            5,000円未満・7日以内で達成できるお手軽案件の攻略情報をお届けします。
          </p>
          <Link href="/category/game-guide" className="cta-box__btn" style={{ animation: 'fadeUp 0.7s var(--ease) 0.9s both', display: 'inline-block' }}>
            ゲーム攻略一覧を見る →
          </Link>
        </div>
      </section>

      {/* Game Guide Section */}
      <section className="section game-guide-section" style={{ background: 'var(--color-bg)' }}>
        <div className="container">
          <div className="game-guide-section__header">
            <span className="section__label">GAME GUIDE</span>
            <h2 className="section__title">🎮 ゲーム攻略（時給効率特化）</h2>
            <p className="section__subtitle">
              7日以内・5,000円未満のお手軽案件のみ。報酬÷時間で選ぶ、新しいポイ活のかたち。
            </p>
          </div>

          {gameGuideArticles.length > 0 ? (
            <div className="card-grid">
              {gameGuideArticles.map((article) => (
                <ArticleCard key={article.id} article={article} />
              ))}
            </div>
          ) : (
            <div style={{ textAlign: 'center', padding: '3rem 0', color: 'var(--color-text-light)' }}>
              <p style={{ fontSize: '1.2rem', marginBottom: '0.5rem' }}>🎮 攻略記事を準備中...</p>
              <p style={{ fontSize: '0.9rem' }}>まもなく高時給ゲームの攻略情報を掲載します</p>
            </div>
          )}

          <div className="game-guide-section__cta">
            <Link href="/category/game-guide" className="cta-box__btn">
              攻略記事をすべて見る →
            </Link>
          </div>
        </div>
      </section>


      {/* Latest Articles */}
      <section className="section">
        <div className="container">
          <h2 className="section__title">最新記事</h2>
          <p className="section__subtitle">
            ポイ活の最新情報・攻略・比較をお届け
          </p>

          {articles.length > 0 ? (
            <div className="card-grid">
              {articles.map((article) => (
                <ArticleCard key={article.id} article={article} />
              ))}
            </div>
          ) : (
            <div style={{ textAlign: 'center', padding: '4rem 0', color: '#999' }}>
              <p style={{ fontSize: '1.2rem', marginBottom: '1rem' }}>
                🚀 まもなく記事を公開予定です
              </p>
              <p>microCMSに記事を追加するとここに表示されます。</p>
            </div>
          )}
        </div>
      </section>

      {/* Categories */}
      <section className="section bg-alt">
        <div className="container">
          <h2 className="section__title">カテゴリー</h2>
          <p className="section__subtitle">気になるテーマから探す</p>

          <div className="card-grid" style={{ gridTemplateColumns: 'repeat(auto-fill, minmax(220px, 1fr))' }}>
            {[
              { name: 'ゲーム攻略', slug: 'game-guide', icon: '🎮', desc: '時給効率特化の攻略情報', highlight: true },
              { name: 'ゲーム×ポイ活', slug: 'game-poikatsu', icon: '🕹️', desc: 'ゲームで稼ぐ最新情報', highlight: false },
              { name: 'ポイ活入門', slug: 'beginner', icon: '📖', desc: '初心者向けガイド', highlight: false },
              { name: 'ランキング・比較', slug: 'ranking', icon: '🏆', desc: 'サービス比較と評価', highlight: false },
              { name: 'ポイント交換', slug: 'exchange', icon: '💱', desc: 'お得な交換先を解説', highlight: false },
              { name: '安全性', slug: 'safety', icon: '🛡️', desc: '安全なポイ活の方法', highlight: false },
            ].map((cat) => (
              <Link
                key={cat.slug}
                href={`/category/${cat.slug}`}
                style={{
                  background: cat.highlight
                    ? 'linear-gradient(135deg, #091D5D 0%, #0e2d8a 100%)'
                    : 'white',
                  borderRadius: 'var(--radius-lg)',
                  padding: 'var(--space-xl)',
                  textAlign: 'center',
                  textDecoration: 'none',
                  border: cat.highlight ? '2px solid #9CD100' : '1px solid var(--color-border-light)',
                  transition: 'transform 0.25s ease, box-shadow 0.25s ease',
                  display: 'block',
                  boxShadow: cat.highlight ? '0 4px 20px rgba(9,29,93,0.25)' : undefined,
                }}
              >
                <div style={{ fontSize: '2.5rem', marginBottom: 'var(--space-sm)' }}>{cat.icon}</div>
                <div style={{
                  fontWeight: 700,
                  color: cat.highlight ? '#9CD100' : 'var(--color-primary)',
                  marginBottom: 'var(--space-xs)',
                }}>
                  {cat.name}
                </div>
                <div style={{
                  fontSize: 'var(--text-sm)',
                  color: cat.highlight ? 'rgba(255,255,255,0.7)' : 'var(--color-text-muted)',
                }}>
                  {cat.desc}
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="section">
        <div className="container">
          <div className="cta-box">
            <div className="cta-box__title">ポイカジで30秒ポイ活を体験しよう</div>
            <p className="cta-box__desc">
              メダルゲームのような興奮を味わいながら、ポイントが貯まる。<br />
              作業感ゼロの新しいポイ活を始めませんか？
            </p>
            <a href="/poicasi" className="cta-box__btn">
              ポイカジの詳細を見る →
            </a>
          </div>
        </div>
      </section>
    </>
  );
}

