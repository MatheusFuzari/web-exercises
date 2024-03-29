/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/*.{js,vue,ts}",
    "./pages/**/.*{js,vue,tsc}",
    "./pages/*.{js,vue,tsc}"
  ],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [],
}

