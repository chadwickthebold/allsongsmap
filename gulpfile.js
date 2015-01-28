var gulp = require('gulp');

// Include Plugins
var concat = require('gulp-concat'),
		rename = require('gulp-rename'),
		jshint = require('gulp-jshint'),
		uglify = require('gulp-uglify'),
//		less = require('gulp-less'), 
		mocha = require('gulp-mocha'),
		shell = require('gulp-shell'),
		merge = require('merge-stream');


// Task to install bower components
gulp.task('bower', shell.task([
	'bower install'
]));

// Initialize the database, requires input
gulp.task('syncdb', shell.task([
	'python manage.py syncdb'
]));

// load the latest stories and artists into the db
gulp.task('initdb', shell.task([
	'python manage.py updateNPR',
	'python manage.py updateArtists'
]));

// Serve a local copy of the project
gulp.task('devserv', shell.task([
	'python manage.py runserver 0.0.0.0:8000'
]));

// Mode the static resources into the musicmapper app
gulp.task('deploy_static', function() {
	var backbone = gulp.src('bower_components/backbone/backbone.js')
		.pipe(gulp.dest('musicmapper/static/js'));

	var underscore = gulp.src('bower_components/underscore/underscore.js')
		.pipe(gulp.dest('musicmapper/static/js'));

	var react = gulp.src('bower_components/react/react.js')
		.pipe(gulp.dest('musicmapper/static/js'));

	var jsx = gulp.src('bower_components/react/JSXTransformer.js')
		.pipe(gulp.dest('musicmapper/static/js'));

var normalize = gulp.src('bower_components/normalize.css/normalize.css')
		.pipe(gulp.dest('musicmapper/static/css'));

var pure = gulp.src('bower_components/pure/pure.css')
		.pipe(gulp.dest('musicmapper/static/css'));

	return merge(backbone, underscore, react, jsx, normalize, pure);
});

// Define default task
gulp.task('default', function() {
	
});