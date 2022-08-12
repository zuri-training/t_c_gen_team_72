/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./*.html'],
  theme: {
    screens:{
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px'
    },
    extend: {
      colors: {
        darkBlue: '#154ED5',
        lightBlue: 'hsla(222, 82%, 46%, 1)',
        strongBlue: 'hsla(222, 82%, 27%, 1)',
        shadeBlue:  '#8CAFFF',
      },
    },
  },
  plugins: [],
}
