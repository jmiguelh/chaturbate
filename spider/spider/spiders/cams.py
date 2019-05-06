# -*- coding: utf-8 -*-
import scrapy
import datetime


class CamsSpider(scrapy.Spider):
    name = 'cams'
    allowed_domains = ['chaturbate.com']
    start_urls = ['https://pt.chaturbate.com/female-cams/', 
        'https://pt.chaturbate.com/male-cams/',
        'https://pt.chaturbate.com/couple-cams/',
        'https://pt.chaturbate.com/trans-cams/']

    def parse(self, response):
        datahora = str(datetime.datetime.now())
        lista = response.xpath("//*[@id='room_list']/li")
        for cam in lista:
            login = cam.xpath('./a/@href').extract_first().replace('/','')
            url = 'https://pt.chaturbate.com/' + cam.xpath('./a/@href').extract_first()[1:]
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
            
            #self.log(",{7}".format(login, url,idade,sexo,local,espectadores,tempo,classificacao))
            
            yield{
                'DataHora' : datahora,
                'Login' : login, 
                'URL' : url,
                'Idade' : idade,
                'Sexo' : sexo,
                'Local' :local,
                'Espectadores' : espectadores,
                'Tempo' : tempo,
                'Calssificacao' : classificacao}
