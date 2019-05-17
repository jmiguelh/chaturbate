FROM python:3-alpine

LABEL name jmiguelh/chaturbate
LABEL src "https://github.com/jmiguelh/chaturbate"
LABEL creator jmiguelh <jmh@jmh.com.br>
LABEL dockerfile_maintenance jmiguelh
LABEL desc "Teste de Scrapy"

RUN apk add --no-cache python3-dev gcc make openssl-dev libxml2-dev libxslt-dev libffi-dev musl-dev
RUN apk add git && git clone https://github.com/jmiguelh/chaturbate.git chaturbate

WORKDIR /chaturbate

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

VOLUME [ "/chaturbate" ]
ENTRYPOINT [ "python", "runner.py" ]
#CMD ["--help"]
