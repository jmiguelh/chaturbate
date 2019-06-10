# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import spider.firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class SpiderPipeline(object):
    def process_item(self, item, spider):
        self.db.collection(u'chaturbate2').document().set(dict(item))
        return item

    def open_spider(self, spider):
        cred = credentials.Certificate(
            'sincere-charmer-137218-firebase-adminsdk-t7g8n-1a5497bdad.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
