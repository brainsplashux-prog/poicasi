import type { Article } from './microcms';

const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL || 'https://poicasi.co.jp';
const SITE_NAME = 'ポイ活ラボ by ポイカジ';

/** サイト共通のメタデータ生成 */
export function generateSiteMetadata(params?: {
  title?: string;
  description?: string;
  path?: string;
  image?: string;
  type?: 'website' | 'article';
  publishedTime?: string;
  modifiedTime?: string;
}) {
  const {
    title,
    description = 'ゲームで稼ぐ、新しいポイ活。カジュアルゲーム×ポイ活の最新情報・比較・攻略をデータに基づいて発信する次世代ポイ活メディア。',
    path = '',
    image = `${SITE_URL}/og-default.png`,
    type = 'website',
    publishedTime,
    modifiedTime,
  } = params || {};

  const fullTitle = title ? `${title} | ${SITE_NAME}` : SITE_NAME;
  const url = `${SITE_URL}${path}`;

  return {
    title: fullTitle,
    description,
    metadataBase: new URL(SITE_URL),
    alternates: { canonical: url },
    openGraph: {
      title: fullTitle,
      description,
      url,
      siteName: SITE_NAME,
      images: [{ url: image, width: 1200, height: 630 }],
      locale: 'ja_JP',
      type,
      ...(publishedTime && { publishedTime }),
      ...(modifiedTime && { modifiedTime }),
    },
    twitter: {
      card: 'summary_large_image' as const,
      title: fullTitle,
      description,
      images: [image],
    },
    robots: {
      index: true,
      follow: true,
      googleBot: {
        index: true,
        follow: true,
        'max-video-preview': -1,
        'max-image-preview': 'large' as const,
        'max-snippet': -1,
      },
    },
  };
}

/** 記事ページのJSON-LD構造化データ生成 */
export function generateArticleJsonLd(article: Article) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Article',
    headline: article.title,
    description: article.description,
    datePublished: article.publishedAt,
    dateModified: article.updatedAt,
    author: {
      '@type': 'Person',
      name: article.author?.name || 'ポイ活ラボ編集部',
    },
    publisher: {
      '@type': 'Organization',
      name: SITE_NAME,
      url: SITE_URL,
      logo: {
        '@type': 'ImageObject',
        url: `${SITE_URL}/logo.png`,
      },
    },
    mainEntityOfPage: {
      '@type': 'WebPage',
      '@id': `${SITE_URL}/articles/${article.slug}`,
    },
    ...(article.eyecatch && {
      image: {
        '@type': 'ImageObject',
        url: article.eyecatch.url,
        width: article.eyecatch.width,
        height: article.eyecatch.height,
      },
    }),
  };
}

/** FAQPage JSON-LD */
export function generateFAQJsonLd(faqs: { question: string; answer: string }[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map((faq) => ({
      '@type': 'Question',
      name: faq.question,
      acceptedAnswer: {
        '@type': 'Answer',
        text: faq.answer,
      },
    })),
  };
}

/** HowTo JSON-LD */
export function generateHowToJsonLd(params: {
  name: string;
  description: string;
  steps: { name: string; text: string }[];
  totalTime?: string;
}) {
  return {
    '@context': 'https://schema.org',
    '@type': 'HowTo',
    name: params.name,
    description: params.description,
    ...(params.totalTime && { totalTime: params.totalTime }),
    step: params.steps.map((step, i) => ({
      '@type': 'HowToStep',
      position: i + 1,
      name: step.name,
      text: step.text,
    })),
  };
}

/** Review JSON-LD */
export function generateReviewJsonLd(params: {
  name: string;
  description: string;
  ratingValue: number;
  bestRating?: number;
  author?: string;
}) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Review',
    itemReviewed: {
      '@type': 'SoftwareApplication',
      name: params.name,
      applicationCategory: 'ポイ活アプリ',
    },
    reviewRating: {
      '@type': 'Rating',
      ratingValue: params.ratingValue,
      bestRating: params.bestRating || 5,
    },
    author: {
      '@type': 'Person',
      name: params.author || 'ポイ活ラボ編集部',
    },
    description: params.description,
  };
}

/** WebSite JSON-LD（トップページ用） */
export function generateWebSiteJsonLd() {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: SITE_NAME,
    url: SITE_URL,
    description: 'ゲームで稼ぐ、新しいポイ活。カジュアルゲーム×ポイ活の最新情報を発信。',
    publisher: {
      '@type': 'Organization',
      name: 'ポイカジ',
      url: SITE_URL,
    },
    potentialAction: {
      '@type': 'SearchAction',
      target: `${SITE_URL}/search?q={search_term_string}`,
      'query-input': 'required name=search_term_string',
    },
  };
}

/** BreadcrumbList JSON-LD */
export function generateBreadcrumbJsonLd(items: { name: string; url: string }[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: item.name,
      item: item.url,
    })),
  };
}
