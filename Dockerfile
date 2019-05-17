FROM python:3-alpine

LABEL name jmiguelh/chaturbate
LABEL src "https://github.com/jmiguelh/chaturbate"
LABEL creator jmiguelh
LABEL dockerfile_maintenance jmiguelh
LABEL desc "Teste de Scrapy"

RUN apk add git && git clone https://github.com/jmiguelh/chaturbate.git chaturbate
#RUN git clone https://github.com/jmiguelh/chaturbate.git chaturbate
WORKDIR /chaturbate
RUN apk add --no-cache python3-dev alpine-sdk
#RUN apk add --no-cache gcc make
RUN apk add --no-cache openssl-dev libxml2-dev libxslt-dev libffi-dev
#openldap-dev
#RUN apk add libevent-dev
#RUN apk add libssl-dev 
#RUN apk add libffi-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

VOLUME [ "/chaturbate" ]
# ENTRYPOINT ["sh"]
ENTRYPOINT [ "python", "runner.py" ]
CMD ["--help"]
