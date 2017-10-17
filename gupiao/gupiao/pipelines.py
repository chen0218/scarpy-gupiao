# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from gupiao.items import GupiaoItem
from gupiao.items import GupiaoAllItem
from gupiao.items import GupiaoOneItem
import time
import os

class GupiaoPipeline(object):
    def process_item(self, item, spider):
#        if isinstance(item,GupiaoItem):
#            with open('股票编号与名称.txt','a',encoding='utf-8') as f:
#                f.write(str(item['gp_name_and_id']) + '\n')
        return item

class GupiaoAll(object):

    def process_item(self, item, spider):
        y = time.localtime().tm_year
        m = time.localtime().tm_mon
        d = time.localtime().tm_mday
        out_file = 'E:/金融/爬取的股票数据/' + str(y) + str(m) + str(d) +'.txt'
        if isinstance(item,GupiaoAllItem):
            with open(out_file,'a',encoding='utf-8') as f:
                f.write(str(item['gp_name']) + ' , ')
                f.write(str(item['gp_yesterday_price']) + ' , ')
                f.write(str(item['gp_start_price']) + ' , ')
                f.write(str(item['gp_max']) + ' , ')
                f.write(str(item['gp_min']) + ' , ')
                f.write(str(item['gp_zf']) + ' , ')
                f.write(str(item['gp_cjl']) + ' , ')
                f.write(str(item['gp_cje']) + ' , ')
                f.write(str(item['gp_np']) + ' , ')
                f.write(str(item['gp_wp']) + ' , ')
                f.write(str(item['gp_wb']) + ' , ')
                f.write(str(item['gp_lb']) + ' , ')
                f.write(str(item['gp_hsl']) + ' , ')
                f.write(str(item['gp_zsz']) + ' , ')
                f.write(str(item['gp_ltsz']) + ' , ')
                f.write(str(item['gp_sjl']) + ' , ')
                f.write(str(item['gp_ltgb']) + ' , ')
                f.write(str(item['gp_syl']) + ' , ')
                f.write(str(item['gp_zgb']) + ' , ')
                f.write(str(item['gp_mgjzc']) + '\n')
        return item


#保存单只股票当天交易明细
class SaveOneGupiao(object):
    def process_item(self, item, spider):
        y = time.localtime().tm_year
        m = time.localtime().tm_mon
        d = time.localtime().tm_mday
        if isinstance(item,GupiaoOneItem):
            out_file1 = 'E:/金融/爬取的股票数据/交易明细/'+str(item['one_id'])
            if not os.path.exists(out_file1):
                os.mkdir(out_file1)
            out_file = out_file1+'/' + str(y) + str(m) + str(d) +'.txt'
            with open(out_file,'a',encoding='utf-8') as f:
                f.write(str(item['deal_time']) + ' , ')
                f.write(str(item['deal_price']) + ' , ')
                f.write(str(item['deal_num']) + ' , ')
                f.write(str(item['deal_1']) + ' , ')
                f.write(str(item['deal_2']) + ' , ')
                f.write(str(item['deal_3']) + ' , ')
                f.write(str(item['deal_4']) + ' , ')
                f.write(str(item['deal_5']) + '\n')


