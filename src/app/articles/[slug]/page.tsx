import { notFound } from 'next/navigation';
import { getArticleBySlug, getAllArticleSlugs, getRelatedArticles } from '@/lib/microcms';
import { generateSiteMetadata, generateArticleJsonLd, generateBreadcrumbJsonLd } from '@/lib/seo';
import ArticleCard from '@/components/ArticleCard';
import ReadingProgress from '@/components/ReadingProgress';
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

// HTMLからH2見出しを抽出してTOCを生成
function extractHeadings(html: string): { id: string; text: string }[] {
  const regex = /<h2[^>]*>(.*?)<\/h2>/gi;
  const headings: { id: string; text: string }[] = [];
  let match;
  let index = 0;
  while ((match = regex.exec(html)) !== null) {
    const text = match[1].replace(/<[^>]*>/g, '').trim();
    headings.push({
      id: `section-${index}`,
      text,
    });
    index++;
  }
  return headings;
}

// HTMLのH2にidを付与
function addIdsToHeadings(html: string): string {
  let index = 0;
  return html.replace(/<h2([^>]*)>/gi, () => {
    const id = `section-${index}`;
    index++;
    return `<h2 id="${id}">`;
  });
}

// 読了時間の計算（日本語: 約500文字/分）
function calculateReadingTime(html: string): number {
  const text = html.replace(/<[^>]*>/g, '');
  const charCount = text.length;
  return Math.max(1, Math.ceil(charCount / 500));
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

  const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || 'https://media.poicasi.co.jp';

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

  // TOC & Reading Time
  const headings = extractHeadings(article.content);
  const contentWithIds = addIdsToHeadings(article.content);
  const readingTime = calculateReadingTime(article.content);

  return (
    <>
      {/* Reading Progress Bar */}
      <ReadingProgress />

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
            <span className="article__reading-time">⏱️ 約{readingTime}分で読めます</span>
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

        {/* Table of Contents */}
        {headings.length > 2 && (
          <nav className="toc">
            <div className="toc__title">目次</div>
            <ul className="toc__list">
              {headings.map((heading) => (
                <li key={heading.id}>
                  <a href={`#${heading.id}`}>{heading.text}</a>
                </li>
              ))}
            </ul>
          </nav>
        )}

        {/* Body */}
        <div
          className="article__body"
          dangerouslySetInnerHTML={{ __html: contentWithIds }}
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
