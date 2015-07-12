var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch');
var minifycss = require('gulp-minify-css');
var livereload = require('gulp-livereload');
var plumber = require('gulp-plumber');


// handle errors without crashing
var onError = function (err) {
  console.log(err);
  this.emit('end');
};

// run sass compress, report errors, and livereload
gulp.task('sass', function() {
    return gulp.src('chipy_voter/static/src/scss/*.scss')
        .pipe(plumber({
            errorHandler: onError
         }))
        .pipe(sass())
        .pipe(gulp.dest('chipy_voter/static/css/'))
        .pipe(livereload());
});

// watch for changes to scss
gulp.task('watch', function() {
  livereload.listen();
  gulp.watch('chipy_voter/static/src/**/*.scss', ['sass']);
});

// Default Task
gulp.task('default', ['sass', 'watch']);
