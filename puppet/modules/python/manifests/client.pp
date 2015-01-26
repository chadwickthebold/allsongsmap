# Install python to current version

class python::client {

	package { "python":
		ensure => $v_python,
		require => Exec["apt-upgrade"],
	}

}