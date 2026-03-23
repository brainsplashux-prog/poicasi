import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'images.microcms-assets.io',
      },
    ],
  },
  // Vercel向け最適化
  poweredByHeader: false,
  compress: true,
};

export default nextConfig;
