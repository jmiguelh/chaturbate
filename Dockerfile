FROM python:3-alpine

LABEL name jmiguelh/chaturbate
LABEL src "https://github.com/jmiguelh/chaturbate"
LABEL creator jmiguelh <jmh@jmh.com.br>
LABEL dockerfile_maintenance jmiguelh
LABEL desc "Scrapy Chaturbate.com"
LABEL version="0.0.2"

#RUN pip install --upgrade pip
RUN apk add --no-cache git --virtual mypacks \
    && git clone https://github.com/jmiguelh/chaturbate.git chaturbate \
    && apk del mypacks
WORKDIR /chaturbate
RUN apk add --no-cache \
    libxml2-dev \
    libxslt-dev \
    libffi-dev 
RUN apk add --no-cache --virtual mypacks \
    python3-dev \
    gcc \
    make \
    openssl-dev \
    musl-dev \
    && pip install -r requirements.txt \
    && apk del mypacks

#VOLUME [ "/chaturbate" ]
ENTRYPOINT [ "python", "runner.py" ]
#CMD ["runner.py"]
