import Link from 'next/link';

export default function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="footer">
      <div className="footer__inner">
        <div>
          <div className="footer__brand">ポイ活ラボ by ポイカジ</div>
          <p className="footer__desc">
            ゲームで稼ぐ、新しいポイ活。<br />
            カジュアルゲーム×ポイ活の最新情報・比較・攻略を<br />
            データに基づいて発信する次世代ポイ活メディア。
          </p>
        </div>

        <div className="footer__section">
          <h4>カテゴリー</h4>
          <ul>
            <li><Link href="/category/game-poikatsu">ゲーム×ポイ活</Link></li>
            <li><Link href="/category/beginner">ポイ活入門</Link></li>
            <li><Link href="/category/ranking">ランキング・比較</Link></li>
            <li><Link href="/category/exchange">ポイント交換</Link></li>
            <li><Link href="/category/safety">安全性</Link></li>
          </ul>
        </div>

        <div className="footer__section">
          <h4>人気記事</h4>
          <ul>
            <li><Link href="/articles/game-poikatsu-guide">ゲームポイ活完全ガイド</Link></li>
            <li><Link href="/articles/poikatsu-beginner">ポイ活の始め方</Link></li>
            <li><Link href="/articles/app-ranking">アプリランキング</Link></li>
          </ul>
        </div>

        <div className="footer__section">
          <h4>サイトについて</h4>
          <ul>
            <li><Link href="/about">ポイ活ラボとは</Link></li>
            <li><Link href="/privacy">プライバシーポリシー</Link></li>
            <li><Link href="/terms">利用規約</Link></li>
            <li><Link href="/contact">お問い合わせ</Link></li>
          </ul>
        </div>
      </div>

      <div className="footer__bottom">
        © {currentYear} ポイ活ラボ by ポイカジ. All Rights Reserved.
      </div>
    </footer>
  );
}
