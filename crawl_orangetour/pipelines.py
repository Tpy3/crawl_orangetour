# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
class CrawlOrangetourPipeline(object):
    def process_item(self, item, spider):
        # pass
        db = MySQLdb.connect(host="127.0.0.1",
                             user="tommy", passwd="scucc",
                             db="tourdata", charset="utf8")
        cursor = db.cursor()

        # 插入資料
        cursor.execute('INSERT INTO crawl_data(pageid,titleid, title_url,title, days,departure_date,price,total,now) '
                       'values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' %
                       (item['pageid'], item['titleid'], item['titleurl'], item['title'], item['days'],
                        item['departure_date'], item['price'], item['total'], item['now']))
        db.commit()
        db.close()
        return item
