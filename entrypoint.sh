#!/bin/sh
set -e

DB_DIR="$(dirname "${SQLITE_PATH:-/app/db.sqlite3}")"
mkdir -p "$DB_DIR" "${MEDIA_ROOT:-/app/media}" /app/static /app/staticfiles

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3
