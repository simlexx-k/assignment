module.exports = {
  darkMode: 'class', // Enable dark mode using the 'class' strategy
  theme: {
    extend: {
      colors: {
        backgroundLight: '#d8e1e6',
        cardBackground: '#f5f5f6',
        borderColor: '#d3d7dd',
        primary: '#3a2d97',
        secondary: '#adadc2',
        textColor: '#000000',
        // Corrected dark theme colors
        dark: {
          background: '#1e293b',
          text: '#f1f5f9',
          border: '#334155',
          primary: '#818cf8',
          secondary: '#a5b4fc',
        },
      },
    },
  },
  plugins: [require('@tailwindcss/forms')], // Add the forms plugin
};