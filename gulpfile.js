const gulp = require('gulp');
const browserSync = require('browser-sync').create();

// File paths
const paths = {
  html: {
    src: 'html/**/*.html'
  },
  css: {
    src: 'css/**/*.+(sass|css)'
  }
};


 
// BrowserSync Serve and Watch task
function serve() {
  browserSync.init({
    server: ''
  });

  // Watch for HTML file changes 
  gulp.watch(paths.html.src).on('change', browserSync.reload);
  gulp.watch(paths.css.src).on('change', browserSync.reload);
}

// Default Gulp task
gulp.task('default', serve);
