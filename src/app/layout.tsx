import type { Metadata } from 'next';
import './globals.css';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import { GoogleAnalytics, MicrosoftClarity } from '@/components/Analytics';
import { generateSiteMetadata, generateWebSiteJsonLd } from '@/lib/seo';

export const metadata: Metadata = generateSiteMetadata();

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const jsonLd = generateWebSiteJsonLd();

  return (
    <html lang="ja">
      <head>
        <link
          href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;600;700;900&family=Inter:wght@400;500;600;700&display=swap"
          rel="stylesheet"
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
      </head>
      <body>
        <GoogleAnalytics />
        <MicrosoftClarity />
        <Header />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
