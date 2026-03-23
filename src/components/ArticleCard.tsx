import Link from 'next/link';
import type { Article } from '@/lib/microcms';

export default function ArticleCard({ article }: { article: Article }) {
  const date = new Date(article.publishedAt).toLocaleDateString('ja-JP', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });

  const categorySlugMap: Record<string, string> = {
    'ゲーム×ポイ活': 'game-poikatsu',
    'ポイ活入門': 'beginner',
    'ポイ活比較': 'ranking',
    'ポイント交換': 'exchange',
    '安全性': 'safety',
  };

  return (
    <Link href={`/articles/${article.slug}`} style={{ textDecoration: 'none' }}>
      <article className="article-card">
        {article.eyecatch ? (
          <img
            src={article.eyecatch.url}
            alt={article.title}
            className="article-card__image"
            width={article.eyecatch.width}
            height={article.eyecatch.height}
            loading="lazy"
          />
        ) : (
          <div
            className="article-card__image"
            style={{
              background: 'linear-gradient(135deg, #091D5D 0%, #1a3a8f 100%)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: '#9CD100',
              fontSize: '1.2rem',
              fontWeight: 700,
            }}
          >
            ポイ活ラボ
          </div>
        )}
        <div className="article-card__body">
          <span className="article-card__category">
            {article.category}
          </span>
          <h3 className="article-card__title">{article.title}</h3>
          <div className="article-card__meta">
            <time dateTime={article.publishedAt}>{date}</time>
            {article.author && <span>{article.author.name}</span>}
          </div>
        </div>
      </article>
    </Link>
  );
}
