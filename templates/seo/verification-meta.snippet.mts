// Meridian template · Search-engine verification meta snippet
// -----------------------------------------------------------
// Merge into `docs/.vitepress/config.mts` `head` array when the user
// provides verification tokens from each search-console portal.
//
// WHY THIS IS A SEPARATE STEP:
//   The user must manually log into each portal to generate the token,
//   then hand it back to the AI. It cannot be automated by Meridian.
//
// USAGE in task 12 Step 9:
//   1. AI prints the instructions (see task-12-discoverability.md Step 9)
//   2. User returns with one or more content strings
//   3. AI uncomments the relevant line(s) below and fills in the value
//   4. AI commits + pushes; CI redeploys; user clicks "Verify" in the portal
//
// None of these are required for Google to index the site — sitemap
// auto-discovery via robots.txt already works. Verification enables the
// portal DASHBOARD (coverage reports, index status, URL inspection).

export const verificationHead: any[] = [
  // Google Search Console — https://search.google.com/search-console
  // ['meta', { name: 'google-site-verification', content: '{{GOOGLE_SITE_VERIFICATION}}' }],

  // Bing Webmaster Tools — https://www.bing.com/webmasters
  // ['meta', { name: 'msvalidate.01', content: '{{BING_SITE_VERIFICATION}}' }],

  // Yandex Webmaster — https://webmaster.yandex.com (optional, for RU audience)
  // ['meta', { name: 'yandex-verification', content: '{{YANDEX_VERIFICATION}}' }],

  // Baidu 站长平台 — https://ziyuan.baidu.com (optional, CN audience; GH Pages IPs
  // are often blocked in CN so indexing is unreliable)
  // ['meta', { name: 'baidu-site-verification', content: '{{BAIDU_VERIFICATION}}' }],
]
