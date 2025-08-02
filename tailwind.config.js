/** @type {import('tailwindcss').Config} */
export default {
  darkMode: ["class"],
  content: [
    './pages/**/*.{js,jsx}',
    './components/**/*.{js,jsx}',
    './app/**/*.{js,jsx}',
    './src/**/*.{js,jsx}',
  ],
  prefix: "",
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      colors: {
        border: "var(--color-border)", /* slate-200 */
        input: "var(--color-input)", /* white */
        ring: "var(--color-ring)", /* blue-600 */
        background: "var(--color-background)", /* gray-50 */
        foreground: "var(--color-foreground)", /* slate-800 */
        primary: {
          DEFAULT: "var(--color-primary)", /* blue-600 */
          foreground: "var(--color-primary-foreground)", /* white */
        },
        secondary: {
          DEFAULT: "var(--color-secondary)", /* slate-500 */
          foreground: "var(--color-secondary-foreground)", /* white */
        },
        destructive: {
          DEFAULT: "var(--color-destructive)", /* red-600 */
          foreground: "var(--color-destructive-foreground)", /* white */
        },
        muted: {
          DEFAULT: "var(--color-muted)", /* slate-100 */
          foreground: "var(--color-muted-foreground)", /* slate-500 */
        },
        accent: {
          DEFAULT: "var(--color-accent)", /* emerald-500 */
          foreground: "var(--color-accent-foreground)", /* white */
        },
        popover: {
          DEFAULT: "var(--color-popover)", /* white */
          foreground: "var(--color-popover-foreground)", /* slate-800 */
        },
        card: {
          DEFAULT: "var(--color-card)", /* white */
          foreground: "var(--color-card-foreground)", /* slate-800 */
        },
        success: {
          DEFAULT: "var(--color-success)", /* emerald-600 */
          foreground: "var(--color-success-foreground)", /* white */
        },
        warning: {
          DEFAULT: "var(--color-warning)", /* amber-600 */
          foreground: "var(--color-warning-foreground)", /* white */
        },
        error: {
          DEFAULT: "var(--color-error)", /* red-600 */
          foreground: "var(--color-error-foreground)", /* white */
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      fontFamily: {
        heading: ['Inter', 'system-ui', 'sans-serif'], /* Inter for headings */
        body: ['Inter', 'system-ui', 'sans-serif'], /* Inter for body text */
        caption: ['Inter', 'system-ui', 'sans-serif'], /* Inter for captions */
        mono: ['JetBrains Mono', 'Consolas', 'monospace'], /* JetBrains Mono for data */
      },
      fontSize: {
        'nav-label': ['12px', { lineHeight: '16px', letterSpacing: '0.04em', fontWeight: '500' }], /* Navigation labels */
        'nav-active': ['14px', { lineHeight: '20px', letterSpacing: '0.04em', fontWeight: '500' }], /* Active navigation */
      },
      boxShadow: {
        'elevation-1': 'var(--shadow-sm)', /* 0 1px 3px rgba(0,0,0,0.1) */
        'elevation-2': 'var(--shadow-md)', /* 0 4px 12px rgba(0,0,0,0.1) */
        'elevation-3': 'var(--shadow-lg)', /* 0 8px 24px rgba(0,0,0,0.12) */
        'chat': 'var(--shadow-chat)', /* 0 2px 8px rgba(0,0,0,0.1) */
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
        "fade-in": "fade-in 0.3s ease-in-out",
        "slide-up": "slide-up 0.3s ease-in-out",
        "shimmer": "shimmer 2s linear infinite",
        "scale-in": "scale-in 0.2s ease-out",
        "stagger-in": "stagger-in 0.4s ease-in-out",
      },
      keyframes: {
        "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
        "fade-in": {
          from: { opacity: "0" },
          to: { opacity: "1" },
        },
        "slide-up": {
          from: { transform: "translateY(10px)", opacity: "0" },
          to: { transform: "translateY(0)", opacity: "1" },
        },
        "shimmer": {
          "0%": { backgroundPosition: "-200px 0" },
          "100%": { backgroundPosition: "calc(200px + 100%) 0" },
        },
        "scale-in": {
          from: { transform: "scale(0.95)", opacity: "0" },
          to: { transform: "scale(1)", opacity: "1" },
        },
        "stagger-in": {
          from: { transform: "translateY(20px)", opacity: "0" },
          to: { transform: "translateY(0)", opacity: "1" },
        },
      },
      transitionDuration: {
        'fast': '200ms', /* Hover states */
        'normal': '300ms', /* Transitions */
        'slow': '400ms', /* Complex state changes */
      },
      transitionTimingFunction: {
        'ease-out-custom': 'cubic-bezier(0.16, 1, 0.3, 1)',
      },
      spacing: {
        'nav-height': '60px', /* Bottom navigation height */
        'header-height': '56px', /* Header height */
        'sidebar-width': '240px', /* Desktop sidebar width */
      },
      zIndex: {
        'navigation': '100', /* Bottom tabs */
        'header': '90', /* Header bar */
        'floating': '80', /* Floating chat action */
        'notification': '110', /* Notification overlays */
        'modal': '120', /* Modals and critical alerts */
      },
    },
  },
  plugins: [
    require("tailwindcss-animate"),
  ],
}