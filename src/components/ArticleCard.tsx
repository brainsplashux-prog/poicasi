import Link from 'next/link';
import type { Article } from '@/lib/microcms';

// content HTML内の最初の画像URLを取得
function extractFirstImage(content: string): string | null {
  const match = content.match(/<img[^>]+src="([^"]+)"/);
  return match ? match[1] : null;
}

// 難易度スター表示
function DifficultyStars({ level }: { level: number }) {
  return (
    <span className="difficulty-stars">
      {[1, 2, 3, 4, 5].map((i) => (
        <span
          key={i}
          className={`difficulty-stars__star ${i <= level ? 'difficulty-stars__star--filled' : 'difficulty-stars__star--empty'}`}
        >
          ★
        </span>
      ))}
    </span>
  );
}

// 時給効率ランク計算
function getEfficiencyRank(rate: number): 'S' | 'A' | 'B' | 'C' {
  if (rate >= 800) return 'S';
  if (rate >= 500) return 'A';
  if (rate >= 300) return 'B';
  return 'C';
}

export default function ArticleCard({ article }: { article: Article }) {
  const date = new Date(article.publishedAt).toLocaleDateString('ja-JP', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });

  const isGameGuide = article.articleType === 'game-guide';

  // eyecatchフィールドがなければcontent内の最初の画像をフォールバック
  const contentImage = extractFirstImage(article.content || '');

  // ゲーム攻略専用フィールド（microCMSのカスタムフィールドとして取得）
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const gameData = article as any;
  const difficulty: number = gameData.gameDifficulty || 0;
  const daysToComplete: string = gameData.gameDaysToComplete || '';
  const maxReward: number = gameData.gameMaxReward || 0;
  const hourlyRate: number = gameData.gameHourlyRate || 0;

  const efficiencyRank = hourlyRate > 0 ? getEfficiencyRank(hourlyRate) : null;

  return (
    <Link href={`/articles/${article.slug}`} style={{ textDecoration: 'none' }}>
      <article className={`article-card${isGameGuide ? ' article-card--game-guide' : ''}`}>
        {article.eyecatch ? (
          <img
            src={article.eyecatch.url}
            alt={article.title}
            className="article-card__image"
            width={article.eyecatch.width}
            height={article.eyecatch.height}
            loading="lazy"
          />
        ) : contentImage ? (
          <img
            src={contentImage}
            alt={article.title}
            className="article-card__image"
            loading="lazy"
          />
        ) : (
          <div
            className="article-card__image"
            style={{
              background: isGameGuide
                ? 'linear-gradient(135deg, #050e40 0%, #0a1f6d 100%)'
                : 'linear-gradient(135deg, #091D5D 0%, #1a3a8f 100%)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: '#9CD100',
              fontSize: '1.2rem',
              fontWeight: 700,
            }}
          >
            {isGameGuide ? '🎮 ゲーム攻略' : 'ポイ活ラボ'}
          </div>
        )}
        <div className="article-card__body">
          <span className="article-card__category">
            {article.category}
          </span>
          <h3 className="article-card__title">{article.title}</h3>

          {/* ゲーム攻略バッジ */}
          {isGameGuide && (
            <div className="article-card__badges">
              {hourlyRate > 0 && efficiencyRank && (
                <span className={`efficiency-badge efficiency-badge--${efficiencyRank.toLowerCase()}`}>
                  時給{hourlyRate.toLocaleString()}円
                </span>
              )}
              {daysToComplete && (
                <span className="days-badge">{daysToComplete}</span>
              )}
              {maxReward > 0 && (
                <span className="badge badge--secondary">
                  最大{maxReward.toLocaleString()}円
                </span>
              )}
              {difficulty > 0 && <DifficultyStars level={difficulty} />}
            </div>
          )}

          <div className="article-card__meta">
            <time dateTime={article.publishedAt}>{date}</time>
            {article.author && <span>{article.author.name}</span>}
          </div>
        </div>
      </article>
    </Link>
  );
}
