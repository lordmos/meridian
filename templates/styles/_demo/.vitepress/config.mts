import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Project Name',
  description: 'Meridian style demo — this page is only used to screenshot each style preset.',
  themeConfig: {
    logo: '/hero.svg',
    nav: [
      { text: 'Docs', link: '/' },
      { text: 'Quick Start', link: '/' },
      { text: 'GitHub', link: 'https://github.com/' },
    ],
  },
})
