#allsongsmap Readme

## About

This is allsongsmap, a webapp that combines the NPR Story API with the Songkick API to figure out if artists featured on the [All Songs Considered](http://www.npr.org/blogs/allsongs/) podcast have upcoming shows in a certain area. The vision is to come to this site, type in your zip code/ city, hit a big 'ol button and get back a list of upcoming events with links to their Songkick page so you can get tickets. Also being explored are sorting featured artists by genre and date, as well as creating a feed so you could just import this whole list right into songkick and have them send you update emails. Rock on! \o/

## Links

* http://www.npr.org/blogs/allsongs/
* https://www.songkick.com/
* http://python-musicbrainzngs.readthedocs.org/en/latest/
* https://github.com/alastair/python-musicbrainzngs
* https://www.songkick.com/developer
* http://www.npr.org/templates/apidoc/
* https://docs.djangoproject.com/en/1.7/
* https://docs.vagrantup.com/v2/getting-started/
* https://sqlite.org/cli.html
* http://puppetlabs.com/puppet/puppet-open-source
* https://docs.vagrantup.com/v2/provisioning/puppet_apply.html

## Vagrant details

Using the ubuntu/trusty64 box. Running apache2, python 2.7.5 and Django 1.7. Also host system should have vagrant >= 1.5 installed.

## Misc Nodes

* gotta start django with python manage.py runserver 0.0.0.0:8000, because apparently 127.0.0.1 is a loopback interface
* sqlite3 commands are prefixed with a period
* allsongsmap = project, musicmapper = app, webapp = client interface, externs = external resources
* all test commands go in /dev folder
* use https://www.hurl.it/ to mock api requests and visualize NPRML response

## Keys

Keys should be stored in keys.prop, which gets cat'd into .bash_profile
```
export NPRKEY='. . .'
export SONGKICKKEY='. . .'
```

## Steps to get project running

1. Clone from bitbucket
2. Ensure Vagrantfile exists and vagrant >= 1.5 is installed on your system
	* vagrant box add ubuntu/trusty64 if necessary
	* Run vagrant up and ensure that all commands executed successfully
3. Run 'manage.py syncdb' to create sqlite tables
	* Use super:pw/user@email.com for development when asked to create superusers

## Logging

Logging is accomplished with pythons built in logging functionality. Inside a command,

```
logger = logging.getLogger(__name__)
logger.info( 'Finished UpdateNPR command in %s:%s:%s' % (hours, minutes, seconds) )
logger.debug( 'blah blah blah')
```
etc...

A matching logging handler needs to have been declared inside the top level settings.py to properly catch stuff.


## Frontend

Here are some details about the frontend-specific stuff.

### Getting started

npm install
gulp bower

### Libraries

Using bower to manage libraries/components

* Backbone
* Backbone-localstorage
* jQuery
* React
* Pure
* Require
* Normalize

### Gulp

Task definitions go in the gulpfile, helpers

#### Dependencies 
* gulp-less
* gulp-rename
* gulp-jshint
* gulp-concat
* gulp-mocha
* gulp-uglify

#### Tasks
* init
* concat
* min
* serve
* test
* watch


## API

* /stories/
* /stories/pk/
* /artists/
* /artists/pk

## TODO

- [x] Task (resolution)
- [ ] Implement more robust logging system
- [ ] Fix mbid to resolve case sensitivity issues, not just take top result
- [ ] Clean up cases where musicbrainz search returns wrong result -> Brian Eno/ David Brynne
- [x] Set NPRKEY and SONGKICKKEY environment variables automatically (Pipe keys.prop to bash_profile)
- [x] Update datetime to non-naive (Using pytz)
- [x] Setup puppet provisioning (check out the puppet directory and init.pp)
- [ ] Integrate with Musicbrainz or Echonest API to get artist info and picture, track listsings
- [ ] Create Story cards
- [ ] Create artist cards
- [ ] Create event cards
- [ ] Figure out caching scheme for event and location search results
- [ ] Implement library for location search using zip code
- [ ] Deploy on Linode with security features
- [ ] Migrate development management to a pure gulp setup, route manage.py through this
- [x] Why is gulp-less throwing a missing module error? (Needed to update global npm to include promises module)
- [ ] Update libraries to latest versions, especially Django REST Framework