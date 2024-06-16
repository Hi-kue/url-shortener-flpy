/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js,jsx,ts,tsx}',
    './static/src/**/*'
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      animation: {
        'loop-scroll': 'loop-scroll 50s linear infinite',
        'shimmer': 'shimmer 2s linear infinite'
      },
      keyframes: {
        'loop-scroll': {
            '0%': { transform: 'translateX(0)' },
            '100%': { transform: 'translateX(-100%)' }
        },
        'shimmer': {
          '0%': {
            backgroundPosition: '0% 0%',
          },
          '100%': {
            backgroundPosition: '200% 0%',
          },
        },
      }
    },
  },
  plugins: [],
}
// tailwind.config.js code
// {
//   "animation": {
//   shimmer: "shimmer 2s linear infinite"
// },
//   "keyframes": {
//   shimmer: {
//     from: {
//       "backgroundPosition": "0 0"
//     },
//     to: {
//       "backgroundPosition": "-200% 0"
//     }
//   }
// }
// }


