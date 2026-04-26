import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'プライバシーポリシー | ポイ活ラボ by ポイカジ',
  description: 'ポイ活ラボのプライバシーポリシーです。個人情報の取り扱いについて説明しています。',
};

export default function PrivacyPage() {
  return (
    <main className="static-page">
      <div className="container">
        <nav className="breadcrumb" aria-label="パンくずリスト">
          <a href="/">ホーム</a>
          <span className="breadcrumb__sep" />
          <span>プライバシーポリシー</span>
        </nav>
        <article className="static-page__content">
          <h1>プライバシーポリシー</h1>
          <p>ポイ活ラボ by ポイカジ（以下「当サイト」）は、ユーザーの個人情報の取り扱いについて、以下のとおりプライバシーポリシーを定めます。</p>

          <h2>1. 収集する情報</h2>
          <p>当サイトでは、お問い合わせやコメント投稿の際に、氏名・メールアドレス等の個人情報をご提供いただく場合があります。また、Googleアナリティクス等のアクセス解析ツールを使用し、匿名の統計情報を収集しています。</p>

          <h2>2. 情報の利用目的</h2>
          <ul>
            <li>お問い合わせへの回答</li>
            <li>サービスの改善・向上</li>
            <li>統計情報の作成・分析</li>
          </ul>

          <h2>3. Cookieについて</h2>
          <p>当サイトはCookieを使用しています。Cookieはブラウザの設定から無効にすることができますが、一部の機能が利用できなくなる場合があります。</p>

          <h2>4. アクセス解析</h2>
          <p>当サイトはGoogleアナリティクスを使用しています。Googleアナリティクスはデータ収集のためにCookieを使用します。このデータは匿名で収集されており、個人を特定するものではありません。</p>

          <h2>5. 第三者への提供</h2>
          <p>当サイトは、法令に基づく場合を除き、ユーザーの同意なく第三者に個人情報を提供することはありません。</p>

          <h2>6. お問い合わせ</h2>
          <p>プライバシーポリシーに関するお問い合わせは、<a href="/contact">お問い合わせページ</a>からご連絡ください。</p>

          <p className="static-page__updated">最終更新日：2026年4月26日</p>
        </article>
      </div>
    </main>
  );
}
