#!/bin/bash
set -e

python /code/manage.py collectstatic --noinput

python /code/manage.py makemigrations

python /code/manage.py migrate

python /code/manage.py createsuperuser --noinput