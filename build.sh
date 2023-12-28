#!/usr/bin/env bash
# exit on error
set -o errexit
# en bash creara un archivo con los requerements instalados: pip freeze > requerements.txt
pip install -r requerements.txt
# ejecuta la carepta de statics
python manage.py collectstatic --no-input
python manage.py migrate