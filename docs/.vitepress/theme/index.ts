import DefaultTheme from 'vitepress/theme'
import type { EnhanceAppContext } from 'vitepress'
import { startInlineIconsWatcher } from './inline-svg'
import './style.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ router }: EnhanceAppContext) {
    if (typeof window === 'undefined') return
    // Run once DOM is ready and on every route change.
    const boot = () => startInlineIconsWatcher()
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', boot)
    } else {
      boot()
    }
    router.onAfterRouteChange = () => startInlineIconsWatcher()
  },
}
