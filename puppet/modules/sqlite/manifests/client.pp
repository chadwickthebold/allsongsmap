# Install sqlite3

class sqlite::client {

	# tcl8.5 dependency for redis
	package {"sqlite3":
		ensure => "installed",
		require => Exec["apt-upgrade"],
	}

}