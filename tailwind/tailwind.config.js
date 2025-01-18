/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [ 
    '../templates/**/*.{html, js}',
  ],
  theme: {
    extend: {
      colors: {
        'custom-bg': '#0B021A',
      },
    },
  },
  safelist: ['bg-custom-bg'],
  plugins: [],
}

