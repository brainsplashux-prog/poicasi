import { notFound } from 'next/navigation';
import { getArticles, type Article } from '@/lib/microcms';
import { generateSiteMetadata, generateBreadcrumbJsonLd } from '@/lib/seo';
import ArticleCard from '@/components/ArticleCard';
import type { Metadata } from 'next';

// SNSトレンド&時給効率に基づくレコメンドゲーム定義
const RECOMMENDED_GAMES = [
  {
    slug: 'coin-master-poikatsu-guide',
    name: 'コインマスター',
    emoji: '🎰',
    reward: '3,500円',
    days: '3〜5日',
    hourly: '550円/時',
    rank: 'A',
    reason: 'SNS拡散度No.1！デイリー無料スピンで誰でも達成',
    tag: '🔥 SNS人気1位',
    tagColor: '#e85d04',
  },
  {
    slug: 'evertale-poikatsu-guide',
    name: 'エバーテイル',
    emoji: '⚔️',
    reward: '3,500円',
    days: '3〜5日',
    hourly: '583円/時',
    rank: 'A',
    reason: '本格RPG案件で口コミ急増中。短期間・高時給のAランク',
    tag: '📈 口コミ急増',
    tagColor: '#7b2d8b',
  },
  {
    slug: 'viking-rise-poikatsu-guide',
    name: 'バイキングライズ',
    emoji: '⚡',
    reward: '4,500円',
    days: '4〜6日',
    hourly: '560円/時',
    rank: 'A',
    reason: '時給560円・最高額4,500円。ライキン勢に特に人気',
    tag: '💰 最高時給',
    tagColor: '#c8963e',
  },
];

export const revalidate = 60;

// カテゴリ定義
const CATEGORIES: Record<string, {
  name: string;
  description: string;
  icon: string;
  microCmsCategory: string;
  relatedSlugs?: string[];  // 記事不足時に表示する関連カテゴリ
}> = {
  'game-guide': {
    name: 'ゲーム攻略',
    description: '7日以内・5,000円未満で達成できるお手軽ゲーム案件の攻略情報。報酬÷時間の「時給効率」が高い案件のみを厳選掲載。放置系・ストラテジー・パズルなど人気ジャンルを網羅。',
    icon: '🎮',
    microCmsCategory: 'ゲーム攻略',
    relatedSlugs: ['game-poikatsu', 'beginner'],
  },
  'game-poikatsu': {
    name: 'ゲーム×ポイ活',
    description: 'カジュアルゲームで稼ぐポイ活の最新情報・攻略・比較を発信。メダルゲーム系・パズル系など、楽しみながら効率よく稼げるゲーム型ポイ活を徹底解説。',
    icon: '🕹️',
    microCmsCategory: 'ゲーム×ポイ活',
    relatedSlugs: ['game-guide', 'beginner'],
  },
  'beginner': {
    name: 'ポイ活入門',
    description: 'ポイ活初心者向けの完全ガイド。始め方・選び方・続け方を脳科学の知見をもとに丁寧に解説。挫折しない方法がわかります。',
    icon: '📖',
    microCmsCategory: 'ポイ活入門',
    relatedSlugs: ['game-guide', 'ranking'],
  },
  'ranking': {
    name: 'ランキング・比較',
    description: 'ポイ活アプリ・サービスの比較ランキング。稼ぎやすさ・面白さ・安全性など複数軸で徹底評価。',
    icon: '🏆',
    microCmsCategory: 'ポイ活比較',
    relatedSlugs: ['beginner', 'game-guide'],
  },
  'exchange': {
    name: 'ポイント交換',
    description: 'ポイントのお得な交換先・交換方法を解説。PayPay・楽天・Amazonギフトなど、最も効率の良い交換ルートを紹介。',
    icon: '💱',
    microCmsCategory: 'ポイント交換',
    relatedSlugs: ['ranking', 'beginner'],
  },
  'safety': {
    name: '安全性',
    description: '安全にポイ活を続ける方法。詐欺アプリの見分け方、個人情報の守り方、信頼できるサービスの選び方を解説。',
    icon: '🛡️',
    microCmsCategory: '安全性',
    relatedSlugs: ['beginner', 'ranking'],
  },
};

export function generateStaticParams() {
  return Object.keys(CATEGORIES).map((slug) => ({ slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const category = CATEGORIES[slug];
  if (!category) return generateSiteMetadata({ title: 'カテゴリが見つかりません' });

  return generateSiteMetadata({
    title: category.name,
    description: category.description,
    path: `/category/${slug}`,
  });
}

export default async function CategoryPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const category = CATEGORIES[slug];
  if (!category) notFound();

  let articles: Article[] = [];
  try {
    const data = await getArticles({
      category: category.microCmsCategory,
      limit: 50,
    });
    articles = data.contents;
  } catch {
    // microCMS未接続時は空
  }

  const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || 'https://media.poicasi.co.jp';
  const breadcrumbJsonLd = generateBreadcrumbJsonLd([
    { name: 'ホーム', url: siteUrl },
    { name: category.name, url: `${siteUrl}/category/${slug}` },
  ]);

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbJsonLd) }}
      />

      {/* Breadcrumb */}
      <nav className="breadcrumb" aria-label="パンくずリスト">
        <a href="/">ホーム</a>
        <span className="breadcrumb__sep" />
        <span>{category.name}</span>
      </nav>

      {/* Category Hero */}
      {slug === 'game-guide' ? (
        <section className="game-guide-hero">
          <div className="game-guide-hero__inner">
            <div className="game-guide-hero__label">⚡ 時給効率特化メディア</div>
            <h1 className="game-guide-hero__title">
              7日以内・5,000円未満で達成できる<br />
              <em>お手軽ゲームポイ活</em>攻略
            </h1>
            <p className="game-guide-hero__desc">{category.description}</p>
            <div className="game-guide-hero__metrics">
              <div className="game-guide-metric">
                <span className="game-guide-metric__value">7日</span>
                <span className="game-guide-metric__label">以内に達成</span>
              </div>
              <div className="game-guide-metric">
                <span className="game-guide-metric__value">5千円</span>
                <span className="game-guide-metric__label">未満の案件</span>
              </div>
              <div className="game-guide-metric">
                <span className="game-guide-metric__value">時給</span>
                <span className="game-guide-metric__label">効率で厳選</span>
              </div>
            </div>
          </div>
        </section>
      ) : (
        <section className="category-hero">
          <div className="container">
            <div className="category-hero__icon">{category.icon}</div>
            <h1 className="category-hero__title">{category.name}</h1>
            <p className="category-hero__desc">{category.description}</p>
          </div>
        </section>
      )}

      {/* SNSおすすめ3選 — game-guideのみ */}
      {slug === 'game-guide' && (
        <section className="recommend-section">
          <div className="container">
            <div className="recommend-section__header">
              <span className="recommend-section__label">SNS人気 &amp; 時給効率</span>
              <h2 className="recommend-section__title">今すぐ始めるならこの3本</h2>
              <p className="recommend-section__sub">
                X（Twitter）口コミ・時給効率・達成しやすさを総合評価した編集部イチオシ
              </p>
            </div>
            <div className="recommend-grid">
              {RECOMMENDED_GAMES.map((game, i) => {
                const href = `/articles/${game.slug}`;
                return (
                  <a key={game.slug} href={href} className="recommend-card">
                    <div className="recommend-card__rank">#{i + 1}</div>
                    <div
                      className="recommend-card__tag"
                      style={{ background: game.tagColor }}
                    >
                      {game.tag}
                    </div>
                    <div className="recommend-card__emoji">{game.emoji}</div>
                    <h3 className="recommend-card__name">{game.name}</h3>
                    <p className="recommend-card__reason">{game.reason}</p>
                    <div className="recommend-card__stats">
                      <div className="recommend-card__stat">
                        <span className="recommend-card__stat-value">{game.reward}</span>
                        <span className="recommend-card__stat-label">最大報酬</span>
                      </div>
                      <div className="recommend-card__stat">
                        <span className="recommend-card__stat-value">{game.days}</span>
                        <span className="recommend-card__stat-label">達成日数</span>
                      </div>
                      <div className="recommend-card__stat recommend-card__stat--gold">
                        <span className="recommend-card__stat-value">{game.hourly}</span>
                        <span className="recommend-card__stat-label">時給効率</span>
                      </div>
                    </div>
                    <div className="recommend-card__cta">攻略を見る →</div>
                  </a>
                );
              })}
            </div>
          </div>
        </section>
      )}

      {/* Articles */}
      <section className="section">
        <div className="container">
          {articles.length > 0 ? (
            <>
              <div className="section-header-row">
                <h2 className="section-header-row__title">
                  {slug === 'game-guide' ? '📋 全攻略記事一覧' : `${category.name}の記事`}
                </h2>
                <span className="section-header-row__count">{articles.length}件</span>
              </div>
              {/* 記事少ない場合のバナー */}
              {articles.length < 3 && slug !== 'game-guide' && (
                <div className="few-articles-notice">
                  ✨ 現在{articles.length}件公開中！順次記事を追加していきます
                </div>
              )}
              {slug === 'game-guide' && (
                <div className="rank-legend">
                  <span className="rank-legend__label">時給効率ランク：</span>
                  <span className="rank-badge rank-badge--s">S 800円+</span>
                  <span className="rank-badge rank-badge--a">A 500〜799円</span>
                  <span className="rank-badge rank-badge--b">B 300〜499円</span>
                </div>
              )}
              <div className="card-grid">
                {articles.map((article) => (
                  <ArticleCard key={article.id} article={article} />
                ))}
              </div>
            </>
          ) : (
            <div className="empty-state">
              <p className="empty-state__icon">{category.icon}</p>
              <p className="empty-state__title">この記事は鋭意制作中です</p>
              <p className="empty-state__desc">
                より充実したコンテンツをお届けするため制作中です。<br />
                他のカテゴリもぜひご覧ください。
              </p>
              <div className="empty-state__links">
                {(category.relatedSlugs ?? []).map(rs => {
                  const rc = CATEGORIES[rs];
                  if (!rc) return null;
                  return (
                    <a key={rs} href={`/category/${rs}`} className="empty-state__link">
                      {rc.icon} {rc.name}
                    </a>
                  );
                })}
                <a href="/" className="empty-state__link empty-state__link--home">🏠 トップへ戻る</a>
              </div>
            </div>
          )}
        </div>
      </section>
    </>
  );
}
