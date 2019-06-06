
# Chaturbate

[![Docker Image](https://images.microbadger.com/badges/version/jmiguelh/chaturbate.svg)](https://microbadger.com/images/jmiguelh/chaturbate "Docker Image")
[![Docker Image](https://images.microbadger.com/badges/image/jmiguelh/chaturbate.svg)](https://microbadger.com/images/jmiguelh/chaturbate "Docker Image")

Projeto de captura, tratameto e análisre do dados das câmeras do site chaturbate.com

## Versões

 * 0.0.1: Captura das cams ativas.
 * 0.0.2: Implmentação da imagem Docker. Versão de prodção com captura das cams ativas e output em .csv
 * 0.1.0: Utilização do Firebase como banco de dados das cams.

## Docker

Criar imagem:  
 `docker build --no-cache -t jmiguelh/chaturbate .` 

Baixar imagem:  
 `docker pull jmiguelh/chaturbate` 

Rodar imagem:  
 * 0.0.2: `docker run -v $PWD/dados:/chaturbate/dados --rm jmiguelh/chaturbate` 
 * 0.1.0: `docker run --rm jmiguelh/chaturbate` 

## Scrapy

Executar o spider:  
 * 0.0.2: `python runner.py` 
 * 0.1.0: `scrapy crawl cams` 

