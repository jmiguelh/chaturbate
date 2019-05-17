FROM scrapinghub/scrapinghub-stack-scrapy:1.6-py3

LABEL name chaturbate
LABEL src "https://github.com/jmiguelh/chaturbate"
LABEL creator jmiguelh
LABEL dockerfile_maintenance jmiguelh
LABEL desc "Teste de Scrapy"

#RUN apk add git && git clone https://github.com/jmiguelh/chaturbate.git Photon
RUN git clone https://github.com/jmiguelh/chaturbate.git chaturbate
WORKDIR chaturbate
RUN pip install -r requirements.txt

VOLUME [ "/chaturbate" ]
# ENTRYPOINT ["sh"]
ENTRYPOINT [ "python", "runner.py" ]
CMD ["--help"]
