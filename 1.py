import requests
import pymysql
import requests
import json
import time, datetime
import urllib.request, urllib.parse, urllib.error
import ssl
import os
from urllib.parse import unquote
from bs4 import BeautifulSoup
from lxml import html
import xml.etree.ElementTree as ET
headers = {
    'authority': 'm.weibo.cn',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'upgrade-insecure-requests': '1',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-dest': 'empty',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
    'cookie': '_T_WM=86587636557; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFGSFbb4n4m7PBERboEl0a35NHD95QfSoncehBX1h-XWs4DqcjlIPS0MNSfdJiLdKBcS0-f; SUB=_2A25NXRqlDeRhGeNI41QR9CrEzjiIHXVuoabtrDV6PUJbktANLRPXkW1NSDCTvCITX-7NKbUcUgtNOzhfQfA42vwi; SSOLoginState=1616472821; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4606042384114943%26luicode%3D20000174%26lfid%3D231051_-_fans_-_6529876887; XSRF-TOKEN=a369c7',
}


for i in range(1,10):
    response = requests.get('https://m.weibo.cn/api/attitudes/show?id=4615677387998143&page='+str(i), headers=headers)
    dd=json.dumps(response.text.encode('utf-8').decode('unicode_escape'))
    c=eval(dd)
    d=json.loads(c)
    for i in d['data']['data']:
        print(str(i['user']['id'])+i['user']['screen_name'])