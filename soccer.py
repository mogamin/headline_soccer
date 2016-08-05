# coding:utf-8
import urllib2 as request
import re
import time
from datetime import datetime
from bs4 import BeautifulSoup
import mylogger
import shelve

HEADER = {  'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8',
            'Keep-Alive' : '300',
            'Connection' : 'keep-alive'
}


def logging(message):
    print datetime.now(), message
    
if __name__ == '__main__':
    logger = mylogger.getMyLogger('')

    req = request.Request('http://live.sportsnavi.yahoo.co.jp/rio2016/live/6386/',None, HEADER)
    body = request.urlopen(req).read()
    soup = BeautifulSoup(body, 'html.parser')
    new_headline = soup.find('p', class_='pickupGameText').text
    
    dic = shelve.open('_headline')
    old_headline = dic['text']
    dic.close()

    if new_headline == old_headline:
        logger.debug("same message:"+new_headline)
    else:
        dic = shelve.open('_headline')
        dic['text'] = new_headline
        dic.close()
        logger.info("new message:"+new_headline)
        
    
