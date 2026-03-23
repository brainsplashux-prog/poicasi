import Link from 'next/link';
import { getArticles, type Article } from '@/lib/microcms';
import ArticleCard from '@/components/ArticleCard';

export const revalidate = 60; // ISR: 60秒ごとに再検証

export default async function Home() {
  let articles: Article[] = [];
  try {
    const data = await getArticles({ limit: 12 });
    articles = data.contents;
  } catch {
    // microCMS未設定時はダミーデータなしで表示
  }

  return (
    <>
      {/* Hero */}
      <section className="hero">
        <div className="hero__inner">
          <span className="hero__badge">🎮 ゲーム × ポイ活メディア</span>
          <h1 className="hero__title">
            ゲームで稼ぐ、<br />
            <span className="hero__title-accent">新しいポイ活</span>。
          </h1>
          <p className="hero__desc">
            カジュアルゲーム×ポイ活の最新情報・比較・攻略を、
            データに基づいて発信。作業感ゼロで楽しみながら
            効率よくポイントを獲得する方法をお届けします。
          </p>
          <Link href="/category/game-poikatsu" className="cta-box__btn">
            ゲームポイ活を始める →
          </Link>
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
              { name: 'ゲーム×ポイ活', slug: 'game-poikatsu', icon: '🎮', desc: 'ゲームで稼ぐ最新情報' },
              { name: 'ポイ活入門', slug: 'beginner', icon: '📖', desc: '初心者向けガイド' },
              { name: 'ランキング・比較', slug: 'ranking', icon: '🏆', desc: 'サービス比較と評価' },
              { name: 'ポイント交換', slug: 'exchange', icon: '💱', desc: 'お得な交換先を解説' },
              { name: '安全性', slug: 'safety', icon: '🛡️', desc: '安全なポイ活の方法' },
            ].map((cat) => (
              <Link
                key={cat.slug}
                href={`/category/${cat.slug}`}
                style={{
                  background: 'white',
                  borderRadius: 'var(--radius-lg)',
                  padding: 'var(--space-xl)',
                  textAlign: 'center',
                  textDecoration: 'none',
                  border: '1px solid var(--color-border-light)',
                  transition: 'transform 0.25s ease, box-shadow 0.25s ease',
                  display: 'block',
                }}
              >
                <div style={{ fontSize: '2.5rem', marginBottom: 'var(--space-sm)' }}>{cat.icon}</div>
                <div style={{ fontWeight: 700, color: 'var(--color-primary)', marginBottom: 'var(--space-xs)' }}>{cat.name}</div>
                <div style={{ fontSize: 'var(--text-sm)', color: 'var(--color-text-muted)' }}>{cat.desc}</div>
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
            <a href="https://poicasi.co.jp" className="cta-box__btn" target="_blank" rel="noopener">
              ポイカジを始める →
            </a>
          </div>
        </div>
      </section>
    </>
  );
}
