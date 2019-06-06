FROM python:3-alpine

LABEL name jmiguelh/chaturbate
LABEL src "https://github.com/jmiguelh/chaturbate"
LABEL creator jmiguelh <jmh@jmh.com.br>
LABEL dockerfile_maintenance jmiguelh
LABEL desc "Scrapy Chaturbate.com"
LABEL version="0.1.0"

RUN apk add --no-cache git --virtual mypacks \
    && git clone -b 0.1.0 https://github.com/jmiguelh/chaturbate.git chaturbate \
    && apk del mypacks

WORKDIR /chaturbate/spider

RUN apk add --no-cache \
    libxml2-dev \
    libxslt-dev \
    libffi-dev \
    libstdc++ 

RUN apk add --no-cache --virtual mypacks \
    python3-dev \
    build-base \
    gcc \
    make \
    openssl-dev \
    musl-dev \
    && pip --no-cache-dir install -r /chaturbate/requirements.txt \
    && apk del mypacks

ADD spider/sincere-charmer-137218-firebase-adminsdk-t7g8n-1a5497bdad.json /chaturbate/spider

ENTRYPOINT [ "scrapy", "crawl", "cams" ]
