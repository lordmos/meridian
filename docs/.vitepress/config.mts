import { defineConfig } from 'vitepress'

// ─── SEO / GEO ──────────────────────────────────────────────
const SITE_URL      = 'https://lordmos.github.io/meridian'
const PROJECT_NAME  = 'Meridian'
const DESCRIPTION   = '把项目的 README、多语言、文档站、Logo、AI 工具上下文——这些重复劳动——压缩成一次 AI 会话。'
const OG_IMAGE      = `${SITE_URL}/og.png`
const GITHUB_URL    = 'https://github.com/lordmos/meridian'
const LICENSE       = 'MIT'

const seoHead: any[] = [
  // Open Graph
  ['meta', { property: 'og:site_name',    content: PROJECT_NAME }],
  ['meta', { property: 'og:title',        content: PROJECT_NAME }],
  ['meta', { property: 'og:description',  content: DESCRIPTION }],
  ['meta', { property: 'og:url',          content: SITE_URL }],
  ['meta', { property: 'og:type',         content: 'website' }],
  ['meta', { property: 'og:image',        content: OG_IMAGE }],
  ['meta', { property: 'og:image:width',  content: '1200' }],
  ['meta', { property: 'og:image:height', content: '630' }],
  // Twitter Card
  ['meta', { name: 'twitter:card',        content: 'summary_large_image' }],
  ['meta', { name: 'twitter:title',       content: PROJECT_NAME }],
  ['meta', { name: 'twitter:description', content: DESCRIPTION }],
  ['meta', { name: 'twitter:image',       content: OG_IMAGE }],
  // Canonical
  ['link', { rel: 'canonical', href: SITE_URL }],
  // GEO — llms.txt discovery
  ['link', { rel: 'alternate', type: 'text/plain', title: 'llms.txt', href: `${SITE_URL}/llms.txt` }],
  ['link', { rel: 'alternate', type: 'text/plain', title: 'llms-full.txt', href: `${SITE_URL}/llms-full.txt` }],
  // JSON-LD structured data
  ['script', { type: 'application/ld+json' }, JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'SoftwareApplication',
    name: PROJECT_NAME,
    description: DESCRIPTION,
    url: SITE_URL,
    applicationCategory: 'DeveloperApplication',
    operatingSystem: 'Cross-platform',
    codeRepository: GITHUB_URL,
    license: LICENSE,
    image: OG_IMAGE,
  })],
]

export default defineConfig({
  base: '/meridian/',
  title: 'Meridian',
  titleTemplate: ':title | Meridian',
  description: DESCRIPTION,

  // SEO: generate sitemap.xml
  sitemap: {
    hostname: SITE_URL + '/',
    transformItems(items) {
      return items.map(item => ({
        ...item,
        changefreq: item.url === '' ? 'weekly' : 'monthly',
        priority:   item.url === '' ? 1.0 : 0.7,
      }))
    },
  },

  head: [
    ['link', { rel: 'icon', href: '/meridian/hero.svg', type: 'image/svg+xml' }],
    ...seoHead,
    // Google Search Console verification (applied via task-12 Step 8b workflow)
    ['meta', { name: 'google-site-verification', content: 'JDAD7_0Djk8ErI3P93dZ2nq5ZKrVGxEi6c7eM7xt-IM' }],
  ],

  // 转义 {{变量名}} 避免 Vue 模板编译报错
  markdown: {
    config: (md) => {
      md.core.ruler.push('escape_vue_interpolation', (state) => {
        for (const token of state.tokens) {
          if (token.type === 'inline' && token.children) {
            for (const child of token.children) {
              if (child.type === 'text' || child.type === 'html_inline') {
                child.content = child.content
                  .replace(/\{\{/g, '&#123;&#123;')
                  .replace(/\}\}/g, '&#125;&#125;')
              }
            }
          }
        }
      })
    }
  },

  ignoreDeadLinks: true,

  vite: {
    resolve: { preserveSymlinks: true },
    server: { fs: { strict: false } },
  },

  locales: {
    root: {
      label: '简体中文',
      lang: 'zh-CN',
      themeConfig: {
        nav: [
          { text: '快速开始', link: '/quick-start' },
          { text: 'FAQ', link: '/faq' },
          { text: 'GitHub', link: 'https://github.com/lordmos/meridian' },
        ],
        sidebar: {
          '/': [
            {
              text: '指南',
              items: [
                { text: '快速开始', link: '/quick-start' },
                { text: 'FAQ', link: '/faq' },
              ],
            },
          ],
        },
      },
    },
    en: {
      label: 'English',
      lang: 'en-US',
      link: '/en/',
      themeConfig: {
        nav: [
          { text: 'Quick Start', link: '/en/quick-start' },
          { text: 'FAQ', link: '/en/faq' },
          { text: 'GitHub', link: 'https://github.com/lordmos/meridian' },
        ],
        sidebar: {
          '/en/': [
            {
              text: 'Guide',
              items: [
                { text: 'Quick Start', link: '/en/quick-start' },
                { text: 'FAQ', link: '/en/faq' },
              ],
            },
          ],
        },
      },
    },
    ja: {
      label: '日本語',
      lang: 'ja',
      link: '/ja/',
      themeConfig: {
        nav: [
          { text: 'クイックスタート', link: '/ja/quick-start' },
          { text: 'FAQ', link: '/ja/faq' },
          { text: 'GitHub', link: 'https://github.com/lordmos/meridian' },
        ],
        sidebar: {
          '/ja/': [
            {
              text: 'ガイド',
              items: [
                { text: 'クイックスタート', link: '/ja/quick-start' },
                { text: 'FAQ', link: '/ja/faq' },
              ],
            },
          ],
        },
      },
    },
    'zh-TW': {
      label: '繁體中文',
      lang: 'zh-TW',
      link: '/zh-TW/',
      themeConfig: {
        nav: [
          { text: '快速開始', link: '/zh-TW/quick-start' },
          { text: 'FAQ', link: '/zh-TW/faq' },
          { text: 'GitHub', link: 'https://github.com/lordmos/meridian' },
        ],
        sidebar: {
          '/zh-TW/': [
            {
              text: '指南',
              items: [
                { text: '快速開始', link: '/zh-TW/quick-start' },
                { text: 'FAQ', link: '/zh-TW/faq' },
              ],
            },
          ],
        },
      },
    },
  },

  themeConfig: {
    socialLinks: [
      { icon: 'github', link: 'https://github.com/lordmos/meridian' },
    ],
    search: { provider: 'local' },
    footer: {
      message: 'Built with <a href="https://github.com/lordmos/meridian" target="_blank">Meridian</a> · open-source ops toolkit for Agent projects',
    },
  },
})
