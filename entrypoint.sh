#! /bin/sh

python /to-do-app/src/manage.py migrate
exec python /to-do-app/src/manage.py runserver 0.0.0.0:8080