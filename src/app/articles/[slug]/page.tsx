import { notFound } from 'next/navigation';
import { getArticleBySlug, getAllArticleSlugs, getRelatedArticles } from '@/lib/microcms';
import { generateSiteMetadata, generateArticleJsonLd, generateBreadcrumbJsonLd } from '@/lib/seo';
import ArticleCard from '@/components/ArticleCard';
import type { Metadata } from 'next';

export const revalidate = 60;

// 静的生成用のslug取得
export async function generateStaticParams() {
  try {
    const slugs = await getAllArticleSlugs();
    return slugs.map((slug) => ({ slug }));
  } catch {
    return [];
  }
}

// メタデータ生成
export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  try {
    const article = await getArticleBySlug(slug);
    if (!article) return generateSiteMetadata({ title: '記事が見つかりません' });

    return generateSiteMetadata({
      title: article.title,
      description: article.description,
      path: `/articles/${article.slug}`,
      image: article.eyecatch?.url,
      type: 'article',
      publishedTime: article.publishedAt,
      modifiedTime: article.updatedAt,
    });
  } catch {
    return generateSiteMetadata({ title: '記事が見つかりません' });
  }
}

export default async function ArticlePage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  let article;
  try {
    article = await getArticleBySlug(slug);
  } catch {
    notFound();
  }
  if (!article) notFound();

  const relatedArticles = await getRelatedArticles(article, 3).catch(() => []);

  const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || 'https://poicasi.co.jp';

  const articleJsonLd = generateArticleJsonLd(article);
  const breadcrumbJsonLd = generateBreadcrumbJsonLd([
    { name: 'ホーム', url: siteUrl },
    { name: article.category, url: `${siteUrl}/category/${article.category}` },
    { name: article.title, url: `${siteUrl}/articles/${article.slug}` },
  ]);

  const publishDate = new Date(article.publishedAt).toLocaleDateString('ja-JP', {
    year: 'numeric', month: 'long', day: 'numeric',
  });
  const updateDate = new Date(article.updatedAt).toLocaleDateString('ja-JP', {
    year: 'numeric', month: 'long', day: 'numeric',
  });

  return (
    <>
      {/* JSON-LD */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(articleJsonLd) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbJsonLd) }}
      />

      {/* Breadcrumb */}
      <nav className="breadcrumb" aria-label="パンくずリスト">
        <a href="/">ホーム</a>
        <span className="breadcrumb__sep" />
        <a href={`/category/${article.category}`}>{article.category}</a>
        <span className="breadcrumb__sep" />
        <span>{article.title}</span>
      </nav>

      {/* Article */}
      <article className="article">
        <header className="article__header">
          <span className="article__category">{article.category}</span>
          <h1 className="article__title">{article.title}</h1>
          <div className="article__meta">
            <time dateTime={article.publishedAt}>📅 {publishDate}</time>
            {article.publishedAt !== article.updatedAt && (
              <time dateTime={article.updatedAt}>🔄 更新: {updateDate}</time>
            )}
            {article.author && <span>✍️ {article.author.name}</span>}
          </div>
        </header>

        {/* Eyecatch */}
        {article.eyecatch && (
          <img
            src={article.eyecatch.url}
            alt={article.title}
            width={article.eyecatch.width}
            height={article.eyecatch.height}
            style={{
              width: '100%',
              borderRadius: 'var(--radius-lg)',
              marginBottom: 'var(--space-2xl)',
            }}
          />
        )}

        {/* Body */}
        <div
          className="article__body"
          dangerouslySetInnerHTML={{ __html: article.content }}
        />

        {/* CTA */}
        <div className="cta-box">
          <div className="cta-box__title">ポイカジで30秒ポイ活を体験しよう</div>
          <p className="cta-box__desc">
            作業感ゼロの新しいポイ活を始めませんか？
          </p>
          <a href="https://poicasi.co.jp" className="cta-box__btn" target="_blank" rel="noopener">
            ポイカジを始める →
          </a>
        </div>
      </article>

      {/* Related Articles */}
      {relatedArticles.length > 0 && (
        <section className="section bg-alt">
          <div className="container">
            <h2 className="section__title">関連記事</h2>
            <div className="card-grid">
              {relatedArticles.map((ra) => (
                <ArticleCard key={ra.id} article={ra} />
              ))}
            </div>
          </div>
        </section>
      )}
    </>
  );
}
