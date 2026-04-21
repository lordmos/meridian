// Meridian template · VitePress `head` config snippet
// ---------------------------------------------------
// Merge into `docs/.vitepress/config.mts` under `export default defineConfig({ head: [ ... ] })`.
// Replace `{{…}}` placeholders with real project values before committing.
//
// What this adds:
//   - Open Graph tags (Facebook / LinkedIn / Discord link previews)
//   - Twitter Card tags (Twitter / X link previews)
//   - Canonical URL
//   - JSON-LD SoftwareApplication schema (structured data for search engines)
//   - llms.txt + llms-full.txt hints (GEO — see `templates/llms-txt/`)
//
// All values below should be set from the project's inferred metadata:
//   SITE_URL        — full deployed URL, e.g. "https://lordmos.github.io/meridian"
//   PROJECT_NAME    — e.g. "Meridian"
//   DESCRIPTION     — one-line project description
//   OG_IMAGE_PATH   — path to 1200×630 OG image, e.g. "/meridian/og/glow.png"
//   TWITTER_HANDLE  — optional, project or author Twitter, e.g. "@lordmos"
//   GITHUB_URL      — e.g. "https://github.com/lordmos/meridian"
//   LICENSE         — e.g. "MIT"

const SITE_URL      = '{{SITE_URL}}'
const PROJECT_NAME  = '{{PROJECT_NAME}}'
const DESCRIPTION   = '{{DESCRIPTION}}'
const OG_IMAGE_PATH = '{{OG_IMAGE_PATH}}'
const TWITTER_HANDLE= '{{TWITTER_HANDLE}}'
const GITHUB_URL    = '{{GITHUB_URL}}'
const LICENSE       = '{{LICENSE}}'

export const seoHead = [
  // ---- Open Graph ----
  ['meta', { property: 'og:site_name',  content: PROJECT_NAME }],
  ['meta', { property: 'og:title',      content: PROJECT_NAME }],
  ['meta', { property: 'og:description',content: DESCRIPTION }],
  ['meta', { property: 'og:url',        content: SITE_URL }],
  ['meta', { property: 'og:type',       content: 'website' }],
  ['meta', { property: 'og:image',      content: `${SITE_URL}${OG_IMAGE_PATH}` }],
  ['meta', { property: 'og:image:width',content: '1200' }],
  ['meta', { property: 'og:image:height',content:'630' }],

  // ---- Twitter Card ----
  ['meta', { name: 'twitter:card',       content: 'summary_large_image' }],
  ['meta', { name: 'twitter:title',      content: PROJECT_NAME }],
  ['meta', { name: 'twitter:description',content: DESCRIPTION }],
  ['meta', { name: 'twitter:image',      content: `${SITE_URL}${OG_IMAGE_PATH}` }],
  ...(TWITTER_HANDLE ? [['meta', { name: 'twitter:site', content: TWITTER_HANDLE }]] : []),

  // ---- Canonical ----
  ['link', { rel: 'canonical', href: SITE_URL }],

  // ---- GEO hints: llms.txt discovery ----
  ['link', { rel: 'alternate', type: 'text/plain', title: 'llms.txt', href: `${SITE_URL}/llms.txt` }],
  ['link', { rel: 'alternate', type: 'text/plain', title: 'llms-full.txt', href: `${SITE_URL}/llms-full.txt` }],

  // ---- JSON-LD SoftwareApplication ----
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
    image: `${SITE_URL}${OG_IMAGE_PATH}`,
  })],
]
