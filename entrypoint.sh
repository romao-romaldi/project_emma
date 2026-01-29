#!/bin/bash

# Fail on error , cela garantit que le script s'arrête
# et sort avec un statut d'erreur non nul en cas d'erreur
set -o errexit

# Fail if an undefined variable is used , cela garantit que le script s'arrête
# et sort avec un statut d'erreur non nul si une variable non définie est utilisée
set -o nounset

# Fail if any command in a pipeline fails , cela garanti que le script s'arrête
# et sort avec un statut d'erreur non nul si une commande dans une pipeline échoue
set -o pipefail


exec python manage.py collectstatic --noinput
exec python manage.py migrate --noinput
exec python -m gunicorn --bind 0.0.0.0:8000 --workers 3 core.wsgi:application