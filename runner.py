from scrapy.cmdline import execute

try:
    execute(
        [
            'scrapy',
            'runspider',
            'spider/spider/spiders/cams.py',
            '-o',
            'dados/cams.csv',
            '-t',
            'csv'
        ]
    )
except SystemExit:
    pass