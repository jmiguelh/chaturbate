
# Chaturbate

Projeto de captura, tratameto e análisre do dados das cêmaeras do site chaturbate.com

1- Spider:
    Execução: scrapy runspider spider/spiders/cams.py

## Docker

Photon can be launched using a lightweight Python-Alpine (103 MB) Docker image.

$ git clone https://github.com/s0md3v/Photon.git
$ cd Photon
$ docker build -t photon .
$ docker run -it --name photon photon:latest -u google.com

To view results, you can either head over to the local docker volume, which you can find by running docker inspect photon or by mounting the target loot folder:

$ docker run -it --name photon -v "$PWD:/Photon/google.com" photon:latest -u google.com