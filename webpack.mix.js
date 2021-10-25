/* Mix provides a clean, fluent API for defining some Webpack build steps for your Masonite
applications. By default, we are compiling the CSS file for the application as well as
bundling up all the JS files. */
const mix = require('laravel-mix')
const path = require('path')


mix.js('resources/js/app.js', 'storage/compiled/js').vue()
  .postCss('resources/css/main.css', 'storage/compiled/css', [
    require('tailwindcss'),
  ]).sass('resources/sass/app.scss', 'public/css')

// add an alias to js code
mix.alias({
  "@": path.resolve("resources/js/"),
})

// add version hash in production
if (mix.inProduction()) {
  mix.version()
}
// Disable compilation success notification
mix.disableSuccessNotifications()

// mix.js('resources/js/app.js', 'public/js')
//     .sass('resources/sass/app.scss', 'public/css')
//     .postCss('resources/css/main.css', 'public/css', [
//         require('tailwindcss'),
//     ]);
