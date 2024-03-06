/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**.{js,vue,ts}",
    "./pages/**.{js,vue,ts}"
  ],
  css: ['~assets/css/main.css'],
  theme: {
    extend: {
    },
  },
  plugins: [],
}

