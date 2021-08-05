#!/bin/bash
set -e

python /code/manage.py collectstatic --noinput

python /code/manage.py makemigrations

python /code/manage.py migrate

python /code/manage.py compilemessages

python /code/manage.py createsuperuser --username admin --email travis.cho@mo-vc.com --noinput