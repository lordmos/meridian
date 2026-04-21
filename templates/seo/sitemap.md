# Sitemap setup (VitePress)

VitePress 1.3+ ships sitemap generation built-in. Add the following to `docs/.vitepress/config.mts`:

```ts
export default defineConfig({
  // ...
  sitemap: {
    hostname: '{{SITE_URL}}',   // e.g. 'https://lordmos.github.io/meridian/'
    transformItems(items) {
      // Optional: prioritize home and quick-start
      return items.map(item => ({
        ...item,
        changefreq: item.url === '' ? 'weekly' : 'monthly',
        priority:   item.url === '' ? 1.0 : 0.7,
      }))
    },
  },
})
```

After `npm run docs:build`, VitePress emits `docs/.vitepress/dist/sitemap.xml` automatically.

GitHub Pages will serve it at `{{SITE_URL}}/sitemap.xml`.

## Verification

After deployment:

```bash
curl -s {{SITE_URL}}/sitemap.xml | head -20
curl -s {{SITE_URL}}/robots.txt
```

Both should return 200 with valid content.

## Submit to search engines (optional but recommended)

- **Google Search Console**: https://search.google.com/search-console → Sitemaps → add `{{SITE_URL}}/sitemap.xml`
- **Bing Webmaster Tools**: https://www.bing.com/webmasters → submit sitemap
- **IndexNow** (instant): `curl "https://api.indexnow.org/indexnow?url={{SITE_URL}}&key=<your-key>"`
