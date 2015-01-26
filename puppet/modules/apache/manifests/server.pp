# Install and configure apache HTTP server

class apache::server {

	package { "apache2":
		ensure => "installed",
		require => Exec["apt-upgrade"],
	}

}