
# Chaturbate

[![Docker Image](https://images.microbadger.com/badges/version/jmiguelh/chaturbate.svg)](https://microbadger.com/images/jmiguelh/chaturbate "Docker Image")
[![Docker Image](https://images.microbadger.com/badges/image/jmiguelh/chaturbate.svg)](https://microbadger.com/images/jmiguelh/chaturbate "Docker Image")

Projeto de captura, tratameto e análisre do dados das cêmaeras do site chaturbate.com

## Docker

Criar imagem:  
 `docker build --no-cache -t jmiguelh/chaturbate .` 

Baixar imagem:  
 `docker pull jmiguelh/chaturbate` 

Rodar imagem:  
 `docker run -v $PWD/dados:/chaturbate/dados jmiguelh/chaturbate` 
