import { createClient } from 'microcms-js-sdk';

// microCMS client
export const client = createClient({
  serviceDomain: process.env.MICROCMS_SERVICE_DOMAIN || '',
  apiKey: process.env.MICROCMS_API_KEY || '',
});

// --- Types ---
export type ArticleCategory =
  | 'ゲーム攻略'        // ← 新設: 時給効率特化ゲーム攻略
  | 'ゲーム×ポイ活'
  | 'ポイ活入門'
  | 'ポイ活比較'
  | 'ポイント交換'
  | '安全性';

export type ArticleType = 'pillar' | 'comparison' | 'howto' | 'review' | 'news' | 'game-guide';

// ゲーム攻略記事専用フィールド
export interface GameGuideData {
  /** 難易度 1（超簡単）〜 5（難しい） */
  gameDifficulty?: number;
  /** 達成日数の目安（例: "3〜5日"） */
  gameDaysToComplete?: string;
  /** 総プレイ時間の目安（例: "約4時間"） */
  gameTotalHours?: string;
  /** 最高報酬額（円）— ポイントサイト横断の最大値 */
  gameMaxReward?: number;
  /** 時給効率（円/時）= gameMaxReward ÷ totalHoursNum */
  gameHourlyRate?: number;
  /** 対応ポイントサイト（カンマ区切り、例: "Moppy,ポイントインカム,げん玉"） */
  gamePointSites?: string;
}

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

/** ゲーム攻略記事のslugパターン */
const GAME_GUIDE_SLUG_SUFFIX = 'poikatsu-guide';

/** 記事一覧取得 */
export async function getArticles(params?: {
  limit?: number;
  offset?: number;
  category?: string;
  orders?: string;
}) {
  const { limit = 10, offset = 0, category, orders = '-publishedAt' } = params || {};

  // ゲーム攻略カテゴリ: slugパターンで全記事からフィルタリング
  if (category === 'ゲーム攻略') {
    const all = await client.getList<Article>({
      endpoint: 'articles',
      queries: { limit: 100, offset: 0, orders },
    });
    const gameArticles = all.contents.filter(
      (a) => a.slug && a.slug.includes(GAME_GUIDE_SLUG_SUFFIX)
    );
    return {
      contents: gameArticles.slice(offset, offset + limit),
      totalCount: gameArticles.length,
      offset,
      limit,
    };
  }

  const filters = category ? `category[contains]${category}` : undefined;

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
