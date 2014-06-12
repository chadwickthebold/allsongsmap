module.exports = function(config){
  config.set({

    basePath : '../',

    files : [
      'bower_components/angular/angular.min.js',
      'bower_components/angular-mocks/angular-mocks.js',
      'js/**/*.js',
      'test/unit/**/*.js',

      //jQuery helpers
      'bower_components/jquery/dist/jquery.min.js',
      'bower_components/jasmine-jquery/lib/jasmine-jquery.js',

      //fixtures
      {pattern: 'test/mock/*.json', watched: true, served: true, included: false}
    ],

    autoWatch : true,

    frameworks: ['jasmine'],

    browsers : ['Chrome'],

    plugins : [
            'karma-chrome-launcher',
            'karma-firefox-launcher',
            'karma-jasmine',
            'karma-junit-reporter'
            ],

    junitReporter : {
      outputFile: 'test_out/unit.xml',
      suite: 'unit'
    }

  });
};