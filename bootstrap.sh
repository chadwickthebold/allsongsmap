#!/usr/bin/env bash

apt-get update
apt-get install -y apache2
apt-get install -y python-django
apt-get install -y sqlite3
ln -s /vagrant ./allsongsmap