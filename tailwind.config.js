/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js,jsx,ts,tsx}',
    './static/src/**/*'
  ],
  theme: {
    extend: {
      animation: {
        'loop-scroll': 'loop-scroll 50s linear infinite'
      },
      keyframes: {
        'loop-scroll': {
            '0%': { transform: 'translateX(0)' },
            '100%': { transform: 'translateX(-100%)' }
        }
      }
    },
  },
  plugins: [],
}

