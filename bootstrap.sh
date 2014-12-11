#!/usr/bin/env bash

apt-get update
apt-get upgrade -y
apt-get install -y apache2
apt-get install -y python-django
apt-get install -y python-pip
pip install musicbrainzngs
apt-get install -y sqlite3
ln -s /vagrant ./allsongsmap
ln -s ./allsongsmap/manage.py manage.py