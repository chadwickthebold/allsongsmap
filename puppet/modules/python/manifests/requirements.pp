# Install required python packages

class python::requirements {

      # Install python-pip
      package { "python-pip":
            ensure => "installed",
            require => Exec["apt-upgrade"],
      }

      # Install all of the required python packages

      package { "Django":
            ensure => $v_django,
            provider => pip,
      }

      package { "musicbrainzngs":
            ensure => "installed",
            provider => pip,
      }

      package { "djangorestframework":
            ensure => "installed",
            provider => pip,
      }

      package { "markdown":
            ensure => "installed",
            provider => pip,
      }

      package { "django-filter":
            ensure => "installed",
            provider => pip,
      }

      package { "pytz":
            ensure => "installed",
            provider => pip,
      }

      package { "redis":
            ensure => "installed",
            provider => pip,
            require => Exec["Install redis server"]
      }

      package { "huey":
            ensure => "installed",
            provider => pip,
            require => Package["redis"],
      }
}