# -*- coding: utf-8 -*-
import scrapy
from ..items import CrawlOrangetourItem

class OrangetourSpider(scrapy.Spider):
    name = 'orangetour'

    def payload_data(self,page):
       data={'displayType': 'G','subCd':'','orderCd': '1','pageALL': str(page),'pageGO': '1','pagePGO': '1','waitData': 'false',
             'waitPage': 'false','mGrupCd':'','SrcCls':'','tabList':'', 'regmCd':'', 'regsCd':'','beginDt': '2019/03/10',
             'endDt': '2019/09/10','portCd':'','tdays':'', 'bjt':'', 'carr':'', 'ikeyword':''}
       return data

    def start_requests(self):
        start_urls ='http://www.orangetour.com.tw/EW/GO/GroupList.asp'
        for page in range(1,54):
            data = self.payload_data(page)
            yield scrapy.FormRequest(url=start_urls, encoding='utf-8', formdata=data,meta={'page':page})

    def parse(self, response):
        first = CrawlOrangetourItem()
        page = response.meta['page']
        print(page)
        print('---' * 50)
        for get_titlelist in range(2,22):
            titlelist = response.xpath('//*[@id="listDataAll"]/div[%s]/div//text()'%(get_titlelist)).extract()
            titlelist_url = response.xpath('//*[@id="listDataAll"]/div[%s]/div/div[3]/a/@href' %(get_titlelist)).extract()
            titlelistlen = len(titlelist)
            # print(titlelistlen,titlelist_url,titlelist)
            if titlelistlen == 56:
                first['pageid'] = 'P002'
                first['titleid'] = titlelist[7]
                first['titleurl'] = 'http://www.orangetour.com.tw'+titlelist_url[0]
                first['title'] = titlelist[8].lstrip().replace(' ', '').replace('\n', '').replace('\r','')
                first['days'] = titlelist[30].split('天')[0]
                first['departure_date'] = titlelist[32].replace('/', '-')
                first['price'] = titlelist[40].replace(',', '')
                first['total'] = titlelist[44]
                first['now'] = titlelist[47]
            elif titlelistlen == 57:
                if '\r\n' in titlelist[8]:
                    first['pageid'] = 'P002'
                    first['titleid'] = titlelist[7]
                    first['titleurl'] = 'http://www.orangetour.com.tw' + titlelist_url[0]
                    first['title'] = titlelist[8].lstrip().replace(' ', '').replace('\n', '').replace('\r', '')
                    first['days'] = titlelist[30].split('天')[0]
                    first['departure_date'] = titlelist[32].replace('/', '-')
                    first['price'] = titlelist[40].replace(',', '')
                    first['total'] = titlelist[44]
                    first['now'] = titlelist[47]
                else:
                    first['pageid'] = 'P002'
                    first['titleid'] = titlelist[8]
                    first['titleurl'] = 'http://www.orangetour.com.tw'+titlelist_url[0]
                    first['title'] = titlelist[9].lstrip().replace(' ', '').replace('\n', '').replace('\r','')
                    first['days'] = titlelist[31].split('天')[0]
                    first['departure_date'] = titlelist[33].replace('/', '-')
                    first['price'] = titlelist[41].replace(',', '')
                    first['total'] = titlelist[45]
                    first['now'] = titlelist[48]
            elif titlelistlen == 58:
                first['pageid'] = 'P002'
                first['titleid'] = titlelist[7]
                first['titleurl'] = 'http://www.orangetour.com.tw'+titlelist_url[0]
                first['title'] = titlelist[8].lstrip().replace(' ', '').replace('\n', '').replace('\r','')
                first['days'] = titlelist[32].split('天')[0]
                first['departure_date'] = titlelist[34].replace('/', '-')
                first['price'] = titlelist[42].replace(',', '')
                first['total'] = titlelist[46]
                first['now'] = titlelist[49]
            elif titlelistlen == 59:
                first['pageid'] = 'P002'
                first['titleid'] = titlelist[7]
                first['titleurl'] = 'http://www.orangetour.com.tw'+titlelist_url[0]
                first['title'] = titlelist[8].lstrip().replace(' ', '').replace('\n', '').replace('\r','')
                first['days'] = titlelist[32].split('天')[0]
                first['departure_date'] = titlelist[34].replace('/', '-')
                first['price'] = titlelist[42].replace(',', '')
                first['total'] = titlelist[46]
                first['now'] = titlelist[49]

            yield first