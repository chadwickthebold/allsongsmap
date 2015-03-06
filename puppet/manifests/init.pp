# @author Tyler Chadwick
# @date 25-January-2015

node default{




	# Update and upgrade the apt-get repos before provisioning starts
	exec { "apt-update":
		command => "/usr/bin/apt-get update",
	}

	exec { "apt-upgrade":
		command => "/usr/bin/apt-get upgrade -y",
		require => Exec["apt-update"]
	}

	Exec["apt-upgrade"] -> Package <| |>


	# Install apache HTTP server
	include apache::server


	# Install sqlite3
	include sqlite::client


	# Install redis, which is a dependency for huey, and thus Django
	include redis::client


	# Install python, pip, Django and other required python packages
	include python::client
	include python::requirements

	# Install front end requirements
	# node, npm, gulp
	package { "nodejs":
		ensure => 'installed'
	}

	package { "npm":
		ensure => 'installed'
	}

	exec { "npm-install":
		command => "/usr/bin/npm install -g gulp bower",
		require => Package['npm']
	}


	# Miscellaneous setup tasks
	file { '/home/vagrant/allsongsmap':
		ensure => 'link',
		target => '/vagrant',
	}

	file { '/home/vagrant/manage.py':
		ensure => 'link',
		target => 'allsongsmap/manage.py',
		require => File["/home/vagrant/allsongsmap"],
	}

	file { '/usr/bin/node':
		ensure => 'link',
		target => '/usr/bin/nodejs',
		require => Package['nodejs']
	}

	exec { "Export API keys":
		command => "/bin/cat ./allsongsmap/keys.prop >> .bash_profile",
		require => File["/home/vagrant/allsongsmap"]
	}

	file { "/etc/profile.d/my_test.sh":
		content => 'export NODE_PATH="/usr/local/lib/node_modules"'
	}




}