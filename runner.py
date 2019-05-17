from scrapy.cmdline import execute

try:
    execute(
        [
            'scrapy',
            'runspider',
            'spider/spider/spiders/cams.py',
            '-o',
            'spider/spider/output/cams.csv',
            '-t',
            'csv'
        ]
    )
except SystemExit:
    pass