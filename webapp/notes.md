# allsongsmap webapp notes

This file will contain general setup and development notes concerning the angular project for the frontend of the allsongsmap project.


## Resource Versions

+ jquery 1.11.1 (for jasmine-jquery)
+ jasmine-jquery 1.7 (for mocking json responses per [stackoverflow](http://stackoverflow.com/questions/17370427/loading-a-mock-json-file-within-karmaangularjs-test))


## General Notes

Project needs to be served for json resources to be properly fetched. Also, project needs to be served prior to running e2e tests with npm run protractor.

To get around proxy for bower use:

'''
git config --global url."https://".insteadOf git://
'''

To revert:

'''
git config --global --unset url."https://".insteadOf
'''