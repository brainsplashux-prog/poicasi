import { createClient } from 'microcms-js-sdk';

// microCMS client
export const client = createClient({
  serviceDomain: process.env.MICROCMS_SERVICE_DOMAIN || '',
  apiKey: process.env.MICROCMS_API_KEY || '',
});

// --- Types ---
export type ArticleCategory = 'ゲーム×ポイ活' | 'ポイ活入門' | 'ポイ活比較' | 'ポイント交換' | '安全性';
export type ArticleType = 'pillar' | 'comparison' | 'howto' | 'review' | 'news';

export interface Article {
  id: string;
  title: string;
  slug: string;
  description: string;
  content: string;
  category: ArticleCategory;
  articleType: ArticleType;
  targetKeyword: string;
  eyecatch?: {
    url: string;
    width: number;
    height: number;
  };
  author?: {
    name: string;
    role: string;
    image?: { url: string };
  };
  publishedAt: string;
  updatedAt: string;
  createdAt: string;
  revisedAt: string;
}

export interface ArticleListResponse {
  contents: Article[];
  totalCount: number;
  offset: number;
  limit: number;
}

// --- API Functions ---

/** 記事一覧取得 */
export async function getArticles(params?: {
  limit?: number;
  offset?: number;
  category?: string;
  orders?: string;
}) {
  const { limit = 10, offset = 0, category, orders = '-publishedAt' } = params || {};

  const filters = category ? `category[equals]${category}` : undefined;

  return await client.getList<Article>({
    endpoint: 'articles',
    queries: {
      limit,
      offset,
      filters,
      orders,
    },
  });
}

/** 記事詳細取得（slug） */
export async function getArticleBySlug(slug: string): Promise<Article | null> {
  const data = await client.getList<Article>({
    endpoint: 'articles',
    queries: {
      filters: `slug[equals]${slug}`,
      limit: 1,
    },
  });
  return data.contents[0] || null;
}

/** 記事詳細取得（ID） */
export async function getArticleById(id: string): Promise<Article> {
  return await client.get<Article>({
    endpoint: 'articles',
    contentId: id,
  });
}

/** 全記事のslug取得（sitemap用） */
export async function getAllArticleSlugs(): Promise<string[]> {
  const data = await client.getList<Article>({
    endpoint: 'articles',
    queries: {
      fields: 'slug',
      limit: 100,
    },
  });
  return data.contents.map((a) => a.slug);
}

/** カテゴリー別記事取得 */
export async function getArticlesByCategory(category: ArticleCategory, limit = 10) {
  return await getArticles({ category, limit });
}

/** 関連記事取得（同カテゴリ、自身を除く） */
export async function getRelatedArticles(article: Article, limit = 3) {
  const data = await client.getList<Article>({
    endpoint: 'articles',
    queries: {
      filters: `category[equals]${article.category}[and]id[not_equals]${article.id}`,
      limit,
      orders: '-publishedAt',
    },
  });
  return data.contents;
}
