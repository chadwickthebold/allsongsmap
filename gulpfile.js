var gulp = require('gulp');

// Include Plugins
var concat = require('gulp-concat'),
		rename = require('gulp-rename'),
		jshint = require('gulp-jshint'),
		uglify = require('gulp-uglify'),
//		less = require('gulp-less'), 
		mocha = require('gulp-mocha'),
		shell = require('gulp-shell');


// Task to install bower components
gulp.task('bower', shell.task([
	'bower install'
]));

// Define default task
gulp.task('default', function() {
	
});