#allsongsmap Readme

## Links

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

Using the ubuntu/trusty64 box. Running apache2, python 2.7.4 and Django 1.7. Also host system should have vagrant >= 1.5 installed.

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
	* Use super:pw/info@tylerchadwick.com for development when asked to create superusers

## Logging

Logging is accomplished with pythons built in logging functionality. Inside a command,

```
logger = logging.getLogger(__name__)
logger.info( 'Finished UpdateNPR command in %s:%s:%s' % (hours, minutes, seconds) )
logger.debug( 'blah blah blah')
```
etc...

A matching logging handler needs to have been declared inside the top level settings.py to properly catch stuff.

## TODO

- [ ] Task (resolution)
- [ ] Implement more robust logging system
- [ ] Fix mbid to resolve case sensitivity issues, not just take top result
- [ ] Clean up cases where musicbrainz search returns wrong result -> Brian Eno/ David Brynne
- [*] Set NPRKEY and SONGKICKKEY environment variables automatically (Pipe keys.prop to bash_profile)
- [*] Update datetime to non-naive (Using pytz)
- [ ] Setup puppet provisioning
- [ ] Deploy on Linode with security features