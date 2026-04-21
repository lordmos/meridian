# Meridian Style Library

Five preset visual languages Meridian can render a project in. Each style defines the full visual system — palette, logo variant, typography stack, VitePress theme vars, icon style — not just colors.

All five share the same **M + compass** motif (outer marker + four cardinal ticks + center letter). Each style interprets that motif in its own aesthetic register.

## The five styles

| id | name | tagline | fit |
|----|------|---------|-----|
| [`glow`](glow/) | **Glow** | Gradient aura on deep space | AI / Agent / generative |
| [`minimalist`](minimalist/) | **Minimalist** | Monochrome ink, clean geometry | CLI / libraries / docs-first |
| [`dev-native`](dev-native/) | **Dev-native** | Terminal, but legible | shells / SDKs / infra |
| [`retro-terminal`](retro-terminal/) | **Retro-Terminal** | Amber phosphor, dashed frame, 80s CRT | games / emulators / retro-tech |
| [`enterprise`](enterprise/) | **Enterprise** | Navy medallion, confident geometry | B2B / platforms / compliance |

## Each style directory contains

| file | purpose |
|------|---------|
| `hero.svg` | 200×200 logo **template** with `{{PROJECT_INITIAL}}` placeholder |
| `preview.svg` | Same as `hero.svg` but with `M` substituted — used by README gallery and docs |
| `palette.svg` | 240×48 three-swatch preview for README gallery cards |
| `style.md` | YAML frontmatter (palette / typography / VitePress theme vars) + prose fit guide |

## How Meridian picks a style (task 3)

1. Explore the target project — infer domain (CLI / AI / B2B / retro / docs / etc.)
2. Recommend ONE default style based on that signal
3. Offer all five as alternatives in the AI conversation
4. User picks or accepts default
5. Derive the concrete palette / logo / theme / icon set from the chosen style's manifest

Default mappings:

| project signal | default style |
|----------------|---------------|
| AI / LLM / Agent / generative | `glow` |
| CLI / library / developer tooling | `minimalist` |
| Shell / terminal / SDK / build system | `dev-native` |
| Retro-computing / game / emulator / tracker | `retro-terminal` |
| B2B / platform / compliance / enterprise SaaS | `enterprise` |

User can always override the recommendation.
