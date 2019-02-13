const gulp = require('gulp');
const cleanCSS = require('gulp-clean-css');
const rename = require('gulp-rename');
const { parallel } = require('gulp');
const minify = require('gulp-minify');
const { watch } = require('gulp');
const { task } = require('gulp');


/* ############## */
/* # minify CSS # */
/* ############## */

function minifyCSSMainpage() {
	return gulp.src([
		'mywebsite/mainpage/static/mainpage/css/*.css',
		'!mywebsite/mainpage/static/mainpage/css/*.min.css'
		])
  	.pipe(cleanCSS({compatibility: 'ie8'}))
  	.pipe(rename({
		suffix: '.min'
    	}))
    .pipe(gulp.dest('mywebsite/mainpage/static/mainpage/css'));
}

function minifyCSSTechblog() {
	return gulp.src([
		'mywebsite/techblog/static/techblog/css/*.css',
		'!mywebsite/techblog/static/techblog/css/*.min.css'
	])
  	.pipe(cleanCSS({compatibility: 'ie8'}))
  	.pipe(rename({
		suffix: '.min'
    	}))
	.pipe(gulp.dest('mywebsite/techblog/static/techblog/css'));
}


/* ############# */
/* # minify JS # */
/* ############# */

function minifyJSMainpage() {
	return gulp.src([
		'mywebsite/mainpage/static/mainpage/js/*.js',
		'!mywebsite/mainpage/static/mainpage/js/*.min.js'
	])
  	.pipe(minify({
		ext: {min:'.min.js'},
		noSource: true,
		
	}))
    .pipe(gulp.dest('mywebsite/mainpage/static/mainpage/js')); 
}

function minifyJSTechblog() {
	return gulp.src([
		'mywebsite/techblog/static/techblog/js/*.js',
		'!mywebsite/techblog/static/techblog/js/*.min.js'
	])
  	.pipe(minify({
		ext: {min:'.min.js'},
		noSource: true,
		
	}))
    .pipe(gulp.dest('mywebsite/techblog/static/techblog/js'));
}


/* ############# */
/* # watch CSS # */
/* ############# */

function watchCSSMainpage() {
	watch(
		[
			'mywebsite/mainpage/static/mainpage/css/*.css',
			'!mywebsite/mainpage/static/mainpage/css/*.min.css'
		],
		minifyCSSMainpage
	);
}

function watchCSSTechblog() {
	watch(
		[
			'mywebsite/techblog/static/techblog/css/*.css',
			'!mywebsite/techblog/static/techblog/css/*.min.css'
		],
		minifyCSSTechblog
	);
}


/* ############ */
/* # watch JS # */
/* ############ */

function watchJSMainpage() {
	watch(
		[
			'mywebsite/mainpage/static/mainpage/js/*.js',
			'!mywebsite/mainpage/static/mainpage/js/*.min.js'
		],
		minifyJSMainpage
	);
}

function watchJSTechblog() {
	watch(
		[
			'mywebsite/techblog/static/techblog/js/*.js',
			'!mywebsite/techblog/static/techblog/js/*.min.js'
		],
		minifyJSTechblog
	);
}


/* ################ */
/* # define tasks # */
/* ################ */

exports.default = parallel(minifyCSSMainpage, minifyCSSTechblog, minifyJSMainpage, minifyJSTechblog);
exports.watchAll = parallel(watchCSSMainpage, watchCSSTechblog, watchJSMainpage, watchJSTechblog);