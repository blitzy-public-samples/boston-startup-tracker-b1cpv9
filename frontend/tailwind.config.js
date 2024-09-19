/** @type {import('tailwindcss').Config} */
module.exports = {
  // TODO: Populate the `content` array with the paths to all template files that use Tailwind CSS classes.
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html",
  ],
  theme: {
    extend: {
      // TODO: Define custom colors, fonts, and other design elements according to the application's design specifications.
      colors: {
        // Example custom colors
        'primary': '#3B82F6',
        'secondary': '#10B981',
        'accent': '#F59E0B',
      },
      fontFamily: {
        // Example custom fonts
        'sans': ['Inter', 'sans-serif'],
        'display': ['Poppins', 'sans-serif'],
      },
      // Add more custom theme extensions here
    },
  },
  plugins: [
    // Add any required Tailwind CSS plugins here
  ],
}

// Human tasks:
// 1. Populate the `content` array with the paths to all template files that use Tailwind CSS classes.
// 2. Define custom colors, fonts, and other design elements according to the application's design specifications.