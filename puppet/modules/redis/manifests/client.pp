# Install redis from source

class redis::client {

	# tcl8.5 dependency for redis
	package {"tcl8.5":
		ensure => "installed",
		require => Exec["apt-upgrade"],
	}

	# Unpack tarball
	exec { "Extract redis":
		command => "/bin/tar xzf ${directory_install}/redis/redis-${v_redis}.tar.gz -C ${directory_install}/redis/",
		creates => "${directory_install}/redis/redis-${v_redis}",
		require => Package["tcl8.5"],
	}

	exec { "Make redis":
		command => "/usr/bin/make -C ${directory_install}/redis/redis-${v_redis}/",
		require => Exec["Extract redis"],
	}

	#exec {"Test redis":
	#	command => "/usr/bin/make -C ${directory_install}/redis/redis-${v_redis}/ test",
	#	require => Exec["Make redis"],
	#}

	exec {"Install redis":
		command => "/usr/bin/make -C ${directory_install}/redis/redis-${v_redis}/ install",
	#	require => Exec["Test redis"],
		require => Exec["Make redis"]
	}

	exec {"Install redis server":
		command => "/bin/echo -n ${directory_install}/redis/redis-${v_redis}/utils/install_server.sh",
		require => Exec["Install redis"],
	}

}