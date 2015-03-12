var gulp = require('gulp');

// Include Plugins
var concat = require('gulp-concat'),
		rename = require('gulp-rename'),
		jshint = require('gulp-jshint'),
		uglify = require('gulp-uglify'),
		less = require('gulp-less'), 
		mocha = require('gulp-mocha'),
		shell = require('gulp-shell'),
		merge = require('merge-stream'),
		react = require('gulp-react'),
		del = require('del');



// Task to install bower components
gulp.task('bower', shell.task([
	'bower install'
]));


gulp.task('react', function() {
	gulp.src('musicmapper/static/js/src/*.jsx')
		.pipe(react())
		.pipe(gulp.dest('musicmapper/static/js/dist'));
});


// Serve a local copy of the project
gulp.task('serve', ['dist'], shell.task([
	'python manage.py runserver 0.0.0.0:8000'
]));


// Move the library resources into the musicmapper app
gulp.task('deploy_static', function() {
	var backbone = gulp.src('bower_components/backbone/backbone.js')
		.pipe(gulp.dest('musicmapper/static/js/lib'));

var localstorage = gulp.src('bower_components/backbone.localstorage/backbone.localStorage.js')
		.pipe(gulp.dest('musicmapper/static/js/lib'));

var jquery = gulp.src('bower_components/jQuery/dist/jquery.js')
		.pipe(gulp.dest('musicmapper/static/js/lib'));

var require = gulp.src('bower_components/require/build/require.js')
		.pipe(gulp.dest('musicmapper/static/js/lib'));

	var underscore = gulp.src('bower_components/underscore/underscore.js')
		.pipe(gulp.dest('musicmapper/static/js/lib'));

	var react = gulp.src('bower_components/react/react.js')
		.pipe(gulp.dest('musicmapper/static/js/lib'));

var normalize = gulp.src('bower_components/normalize.css/normalize.css')
		.pipe(gulp.dest('musicmapper/static/css/lib'));

var pure = gulp.src('bower_components/pure/pure.css')
		.pipe(gulp.dest('musicmapper/static/css/lib'));

});


// Compile LESS files into CSS
gulp.task('less', function() {
	gulp.src('musicmapper/static/less/*.less')
		.pipe(less())
		.pipe(gulp.dest('musicmapper/static/css'));
})


// Wipe files generated in build and dist stages
gulp.task('clean', function() {
	del(['musicmapper/static/js/dist', 'musicmapper/static/css'])
});


// Compile and minify static web files
gulp.task('dist', ['react','deploy_static'], function() {
	gulp.src('musicmapper/static/js/src/*.js')
		.pipe(gulp.dest('musicmapper/static/js/dist'));
});


gulp.task('watch', ['dist'], function() {
	gulp.watch('musicmapper/static/js/src/*', ['dist']);
	gulp.watch('musicmapper/static/less/*', ['less']);
});


gulp.task('init', function() {

});


// Compile library and project files into unified files
// This will include running jshint prior to the closure compiler minifying everything
gulp.task('concat', function() {

});


// Minify the compiled static files
gulp.task('min', function() {

});


// Run unit tests
gulp.task('test', function() {

});



// Define default task
// This will deploy static resources
gulp.task('default', ['init', 'concat', 'min', 'serve', 'watch'],function() {
	
});