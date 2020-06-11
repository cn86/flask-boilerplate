#!/bin/bash
set -e

if [ "$1" = 'runserver' ]; then
    sleep 5
    flask db upgrade
    python /app/migrations/seed.py
    exec flask run -h 0.0.0.0 -p 8080
else
    exec "$@"
fi
