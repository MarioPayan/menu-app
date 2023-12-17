/** @type {import('next').NextConfig} */
const nextConfig = {
  images: { // TODO: Replace with the actual domain
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'via.placeholder.com',
        port: '',
        pathname: '**',
      },
    ],
  },
}

module.exports = nextConfig
