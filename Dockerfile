FROM python:3.7-stretch

ENV LANG C.UTF-8

RUN apt-get update -qq && apt-get install -qqy --no-install-recommends \
     openssh-client \
     python3-pip \
     python3-setuptools \
     python3-wheel \
     git \
     build-essential \
     python3-dev

COPY requirements/. /srv/requirements/.

WORKDIR /srv

ARG FLASK_ENV
ENV FLASK_ENV=${FLASK_ENV}

RUN pip3 install -r requirements/${FLASK_ENV}.txt

COPY . /srv/

EXPOSE 5000

ENTRYPOINT ["bash", "./run_app.sh"]
