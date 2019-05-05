# -*- coding: utf-8 -*-
import scrapy


class CamsSpider(scrapy.Spider):
    name = 'cams'
    allowed_domains = ['chaturbate.com']
    start_urls = ['https://pt.chaturbate.com/']

    def parse(self, response):
        lista = response.xpath("//*[@id='room_list']/li")
        for cam in lista:
            login = cam.xpath('./a/@href').extract_first().replace('/','')
            url = response.url + cam.xpath('./a/@href').extract_first()[1:]
            if cam.xpath('./div[3]/div/span/text()').extract_first().isnumeric(): 
                idade = int(cam.xpath('./div[3]/div/span/text()').extract_first())
            else:
                idade = 99 
            sexo = cam.xpath('./div[3]/div/span/@class').extract_first()[-1]
            local = cam.xpath('./div[3]/ul[2]/li[1]/text()').extract_first()
            dados = cam.xpath('./div[3]/ul[2]/li[2]/text()').extract_first().split(' ')
            espectadores = int(dados[-1])
            if dados[1] == "mins":
                tempo =float(int(dados[0])/60)
            else:
                tempo = float(dados[0].replace(',','.'))
            classificacao = cam.xpath('./div[2]/text()').extract_first()
            
            self.log("Login: {0} - URL: {1} - Idade: {2} - Sexo: {3} - Local: {4} - Espectadores: {5} - Tempo: {6} -  Classificação: {7}".format(login, url,idade,sexo,local,espectadores,tempo,classificacao))
            
