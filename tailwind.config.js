/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './appointments/templates/**/*.html', // Adjust paths based on your structure
    './appointments/static/**/*.js',       // If you have any JavaScript files
    // Add any additional paths if needed
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};

