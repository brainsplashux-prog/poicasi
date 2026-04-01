import { notFound } from 'next/navigation';
import { getArticles, type Article } from '@/lib/microcms';
import { generateSiteMetadata, generateBreadcrumbJsonLd } from '@/lib/seo';
import ArticleCard from '@/components/ArticleCard';
import type { Metadata } from 'next';

export const revalidate = 60;

// カテゴリ定義
const CATEGORIES: Record<string, { name: string; description: string; icon: string; microCmsCategory: string }> = {
  'game-poikatsu': {
    name: 'ゲーム×ポイ活',
    description: 'カジュアルゲームで稼ぐポイ活の最新情報・攻略・比較を発信。メダルゲーム系・パズル系など、楽しみながら効率よく稼げるゲーム型ポイ活を徹底解説。',
    icon: '🎮',
    microCmsCategory: 'ゲーム×ポイ活',
  },
  'beginner': {
    name: 'ポイ活入門',
    description: 'ポイ活初心者向けの完全ガイド。始め方・選び方・続け方を脳科学の知見をもとに丁寧に解説。挫折しない方法がわかります。',
    icon: '📖',
    microCmsCategory: 'ポイ活入門',
  },
  'ranking': {
    name: 'ランキング・比較',
    description: 'ポイ活アプリ・サービスの比較ランキング。稼ぎやすさ・面白さ・安全性など複数軸で徹底評価。',
    icon: '🏆',
    microCmsCategory: 'ポイ活比較',
  },
  'exchange': {
    name: 'ポイント交換',
    description: 'ポイントのお得な交換先・交換方法を解説。PayPay・楽天・Amazonギフトなど、最も効率の良い交換ルートを紹介。',
    icon: '💱',
    microCmsCategory: 'ポイント交換',
  },
  'safety': {
    name: '安全性',
    description: '安全にポイ活を続ける方法。詐欺アプリの見分け方、個人情報の守り方、信頼できるサービスの選び方を解説。',
    icon: '🛡️',
    microCmsCategory: '安全性',
  },
};

// 静的生成用のslug取得
export function generateStaticParams() {
  return Object.keys(CATEGORIES).map((slug) => ({ slug }));
}

// メタデータ生成
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
      <section className="category-hero">
        <div className="container">
          <div className="category-hero__icon">{category.icon}</div>
          <h1 className="category-hero__title">{category.name}</h1>
          <p className="category-hero__desc">{category.description}</p>
        </div>
      </section>

      {/* Articles */}
      <section className="section">
        <div className="container">
          {articles.length > 0 ? (
            <>
              <p className="section__subtitle">
                {articles.length}件の記事があります
              </p>
              <div className="card-grid">
                {articles.map((article) => (
                  <ArticleCard key={article.id} article={article} />
                ))}
              </div>
            </>
          ) : (
            <div style={{ textAlign: 'center', padding: '4rem 0', color: '#999' }}>
              <p style={{ fontSize: '3rem', marginBottom: '1rem' }}>{category.icon}</p>
              <p style={{ fontSize: '1.2rem', marginBottom: '0.5rem', fontWeight: 600 }}>
                {category.name}の記事を準備中です
              </p>
              <p style={{ fontSize: '0.9rem' }}>
                まもなく記事を公開予定です。お楽しみにお待ちください。
              </p>
            </div>
          )}
        </div>
      </section>
    </>
  );
}
