#web: python3 manage.py migrate && gunicorn zaduya.wsgi --log-file -
web: gunicorn --bind 0.0.0.0:$PORT project_ema.wsgi:application --log-file -