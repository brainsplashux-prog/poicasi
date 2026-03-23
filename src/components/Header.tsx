'use client';

import Link from 'next/link';
import { useState } from 'react';

const NAV_ITEMS = [
  { label: 'ホーム', href: '/' },
  { label: 'ゲーム×ポイ活', href: '/category/game-poikatsu' },
  { label: 'ポイ活入門', href: '/category/beginner' },
  { label: 'ランキング', href: '/category/ranking' },
  { label: '安全性', href: '/category/safety' },
];

export default function Header() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <header className="header">
      <div className="header__inner">
        <Link href="/" className="header__logo">
          ポイ活<span className="header__logo-accent">ラボ</span>
        </Link>

        <button
          className="header__menu-btn"
          onClick={() => setIsOpen(!isOpen)}
          aria-label="メニュー"
        >
          <span />
          <span />
          <span />
        </button>

        <nav className={`header__nav ${isOpen ? 'open' : ''}`}>
          {NAV_ITEMS.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              onClick={() => setIsOpen(false)}
            >
              {item.label}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
