#!/usr/bin/env bash

apt-get update
apt-get upgrade -y
apt-get install -y apache2
apt-get install -y python-pip
pip install Django
pip install musicbrainzngs
pip install djangorestframework
pip install markdown
pip install django-filter
apt-get install -y sqlite3
ln -s /vagrant ./allsongsmap
cat ./allsongsmap/keys.prop >> .bash_profile
ln -s ./allsongsmap/manage.py manage.py
alias startserver="python manage.py runserver 0.0.0.0:8000"