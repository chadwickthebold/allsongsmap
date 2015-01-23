#!/usr/bin/env bash

apt-get update
apt-get upgrade -y
apt-get install -y apache2
apt-get install -y python-pip
apt-get install -y tcl8.5 # This is a redis requirement

## Gotta install redis somehow here

pip install Django
pip install musicbrainzngs
pip install djangorestframework
pip install markdown
pip install django-filter
pip install pytz
pip install redis # Redis drivers for python/huey
pip install huey
apt-get install -y sqlite3
ln -s /vagrant ./allsongsmap
cat ./allsongsmap/keys.prop >> .bash_profile
ln -s ./allsongsmap/manage.py manage.py
printf '\n alias startserver="python manage.py runserver 0.0.0.0:8000"' >> .bash_profile