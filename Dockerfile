###########
# BUILDER #
###########

# pull official base image
FROM python:3.9.5-slim as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y \
    ca-certificates \
    gcc \
    python3-dev \
    musl-dev \
    zlib1g \
    zlib1g-dev \
    libjpeg62 \
    libjpeg-dev \
    libfreetype6-dev

# install dependencies
COPY . .
RUN pip install --upgrade pip wheel setuptools
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.9.5-slim

# credentials
LABEL version="1.0.0"
LABEL autor="luizfelipevbll@gmail.com"

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system app --ingroup app

# create the appropriate directories
ENV HOME=/home/app
ENV ROOT=/root
RUN mkdir $HOME/media
RUN mkdir $HOME/logs
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

# update packages
RUN apt-get update && apt-get upgrade -y

# install dependencies
RUN apt-get install -y \
    build-essential \
    apt-transport-https \
    bash-completion \
    libpq5 \
    libpq-dev \
    vim \
    curl \
    zlib1g \
    zlib1g-dev \
    libjpeg62 \
    libjpeg-dev \
    libfreetype6-dev \
    ca-certificates

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install -U pip wheel setuptools 
RUN pip install --no-cache /wheels/*

# copy project
COPY . .
# RUN sed -i 's/\r$//g'  $APP_HOME/scripts/entrypoint.sh
# RUN chmod +x  $APP_HOME/scripts/entrypoint.sh

# copy custom .bashrc to new locations
# RUN tee $HOME/.bashrc $ROOT/.bashrc < $APP_HOME/scripts/.bashrc

# chown all the files to the app user
RUN chown -R app:app $HOME

# change to the app user
USER app

# run entrypoint.sh
# ENTRYPOINT ["/home/app/web/scripts/entrypoint.sh"]

# OBS:
# Multi-stage build to reduce the final image size,
# BUILDER is temporary for building Python Wheels, then copying to FINAL image
