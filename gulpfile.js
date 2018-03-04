// requirements

var gulp = require('gulp');
var gulpBrowser = require("gulp-browser");
var reactify = require('reactify');
var del = require('del');
var size = require('gulp-size');
var less = require('gulp-less');
var livereload = require('gulp-livereload');

// tasks
gulp.task('transform', function () {
  var stream = gulp.src('./app/static/scripts/jsx/*.js')
    .pipe(gulpBrowser.browserify({transform: ['reactify']}))
    .pipe(gulp.dest('./app/static/scripts/js/'))
    .pipe(size())
      .pipe(livereload());
  return stream;
});


gulp.task('del', function () {
  return del(['./app/static/scripts/js']);
});


gulp.task('default', ['del'], function() {
    console.log("hello!");
  gulp.start('transform');
  livereload.listen();
  gulp.watch('./app/static/scripts/jsx/*.js', ['transform']);
  gulp.watch('./app/static/less/*.less', ['less']);
});


gulp.task('less', function() {
  gulp.src('./app/static/less/*.less')
    .pipe(less())
    .pipe(gulp.dest('./app/static/css'))
    .pipe(livereload()
    );
});


