#!/bin/bash

rsync -av --delete _site/ root@69.164.219.36:/var/www/pingswept.org/

ssh root@69.164.219.36 "chown -R www-data:www-data /var/www/*"
