import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'お問い合わせ | ポイ活ラボ by ポイカジ',
  description: 'ポイ活ラボへのお問い合わせはこちらから。',
};

export default function ContactPage() {
  return (
    <main className="static-page">
      <div className="container">
        <nav className="breadcrumb" aria-label="パンくずリスト">
          <a href="/">ホーム</a>
          <span className="breadcrumb__sep" />
          <span>お問い合わせ</span>
        </nav>
        <article className="static-page__content">
          <h1>お問い合わせ</h1>
          <p>
            ポイ活ラボ by ポイカジへのご質問・ご要望・記事の誤りの報告などは、
            下記のフォームよりお気軽にご連絡ください。
          </p>
          <p>通常3営業日以内にご返信いたします。</p>

          <div className="contact-form">
            <div className="contact-form__field">
              <label htmlFor="contact-name">お名前 <span className="required">必須</span></label>
              <input id="contact-name" type="text" placeholder="山田 太郎" />
            </div>
            <div className="contact-form__field">
              <label htmlFor="contact-email">メールアドレス <span className="required">必須</span></label>
              <input id="contact-email" type="email" placeholder="example@email.com" />
            </div>
            <div className="contact-form__field">
              <label htmlFor="contact-subject">件名</label>
              <input id="contact-subject" type="text" placeholder="記事の内容についてなど" />
            </div>
            <div className="contact-form__field">
              <label htmlFor="contact-message">メッセージ <span className="required">必須</span></label>
              <textarea id="contact-message" rows={6} placeholder="お問い合わせ内容をご記入ください" />
            </div>
            <button type="submit" className="contact-form__submit">送信する</button>
            <p className="contact-form__note">
              ※ 現在フォームは準備中です。お急ぎの場合はSNSよりご連絡ください。
            </p>
          </div>
        </article>
      </div>
    </main>
  );
}
