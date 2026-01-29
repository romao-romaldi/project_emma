# app/Dockerfile

# pull the official docker image
FROM python:3.13-slim


ARG APP_HOME=/app
ARG APP_USER=fastapi
ARG APP_GROUP=fastapi
ARG USER_ID=1000
ARG GROUP_ID=1000


# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y gcc python3-dev libpq-dev


RUN mkdir ${APP_HOME}
# set work directory
WORKDIR ${APP_HOME}

COPY . ${APP_HOME}

RUN pip install --upgrade pip
COPY requirements.txt /app/
# copy ok

RUN pip install -r requirements.txt
# Exécute la collecte des fichiers statiques pendant le build
# RUN python manage.py collectstatic --noinput

COPY entrypoint.sh ${APP_HOME}/entrypoint.sh

RUN chmod +x ${APP_HOME}/entrypoint.sh
