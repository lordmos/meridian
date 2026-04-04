import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/meridian/',

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
          { text: 'GitHub', link: 'https://github.com/lordmos/meridian' },
        ],
        sidebar: {
          '/': [
            {
              text: '指南',
              items: [
                { text: '快速开始', link: '/quick-start' },
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
          { text: 'GitHub', link: 'https://github.com/lordmos/meridian' },
        ],
        sidebar: {
          '/en/': [
            {
              text: 'Guide',
              items: [
                { text: 'Quick Start', link: '/en/quick-start' },
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
          { text: 'GitHub', link: 'https://github.com/lordmos/meridian' },
        ],
        sidebar: {
          '/ja/': [
            {
              text: 'ガイド',
              items: [
                { text: 'クイックスタート', link: '/ja/quick-start' },
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
          { text: 'GitHub', link: 'https://github.com/lordmos/meridian' },
        ],
        sidebar: {
          '/zh-TW/': [
            {
              text: '指南',
              items: [
                { text: '快速開始', link: '/zh-TW/quick-start' },
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
