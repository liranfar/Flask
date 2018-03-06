// requirements
var gulp = require('gulp');
var del = require('del');
var less = require('gulp-less');
var livereload = require('gulp-livereload');
var open = require('gulp-open');
var babelify = require("babelify");
var browserify = require("browserify");
var uglify = require("gulp-uglify");
var source = require('vinyl-source-stream');
var buffer = require('vinyl-buffer');
var packageJSON = require('./package.json');
var dependencies = Object.keys(packageJSON && packageJSON.dependencies || {});

//Todo: add error handler which prevents the process crushing
// tasks
gulp.task('del', function () {
    return del(['./app/static/scripts/js']);
});


gulp.task('default', ['del','vendor','babelify', 'open'], function() {
    livereload.listen();
    gulp.watch('./app/static/scripts/jsx/**/*.js', ['babelify']);
    gulp.watch('./app/static/less/*.less', ['less']);
});


gulp.task('less', function() {
    gulp.src('./app/static/less/*.less')
        .pipe(less())
        .pipe(gulp.dest('./app/static/css'))
        .pipe(livereload()
    );
});

gulp.task('open', function(){
  gulp.src('/')
  .pipe(open({uri : 'http://localhost:5000'}));
});



gulp.task('babelify', function () {
  browserify('./app/static/scripts/jsx/main.js')
    .transform(babelify.configure({presets: ["es2015" , "react", "stage-3"]}))
    .bundle()
    .pipe(source('index.js'))
    //.pipe(buffer())
    //.pipe(uglify())
    .pipe(gulp.dest('./app/static/scripts/js'))
    .pipe(livereload()
    );
});


gulp.task('vendor', function() {
  return browserify()
    .require(dependencies)
    .bundle()
    .pipe(source('bundle.js'))
    //.pipe(buffer())
    //.pipe(uglify())
    .pipe(gulp.dest('./app/static/scripts/js/vendor'));
});
