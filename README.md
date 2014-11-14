#allsongsmap Readme

## Links

* http://python-musicbrainzngs.readthedocs.org/en/latest/
* https://github.com/alastair/python-musicbrainzngs
* https://www.songkick.com/developer
* http://www.npr.org/templates/apidoc/
* https://docs.djangoproject.com/en/1.6/
* https://docs.vagrantup.com/v2/getting-started/
* https://sqlite.org/cli.html

## Vagrant details

Using the ubuntu/trusty64 box. Running apache2, python 2.7.4 and Django 1.6. Also host system should have vagrant >= 1.5 installed.

## Misc Nodes

* gotta start django with python manage.py runserver 0.0.0.0:8000, because apparently 127.0.0.1 is a loopback interface
* sqlite3 commands are prefixed with a period
* allsongsmap = project, musicmapper = app, webapp = client interface, externs = external resources
* all test commands go in /dev folder

## Steps to get project running

1. Clone from bitbucket
2. Ensure Vagrantfile exists and vagrant >= 1.5 is installed on your system
	* vagrant box add ubuntu/trusty64 if necessary
	* Run vagrant up and ensure that all commands executed successfully
3. Run 'manage.py syncdb' to create sqlite tables
	* Use super:pw/info@tylerchadwick.com for development when asked to create superusers

## TODO

* [ ] logging
* [ ] fix mbid to resolve case sensitivity issues, not just take top result
* [ ] need to clean up cases where musicbrainz search returns wrong result -> Brian Eno/ David Brynne