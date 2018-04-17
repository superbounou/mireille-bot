FROM alpine

MAINTAINER Nicolas Bounoughaz

RUN apk add --update \
    python \
    python-dev \
    py-pip \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

WORKDIR /app

COPY . /app
RUN virtualenv /env && /env/bin/pip install -r /app/requirements.txt

CMD ["/env/bin/python", "project-cli.py"]
