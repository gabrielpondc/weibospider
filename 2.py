import requests

headers = {
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'authority': 'm.weibo.cn',
    'cache-control': 'no-cache',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-dest': 'empty',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
    'cookie': 'SUB=_2A25NXF_SDeRhGeRK6lAX9i7KyDmIHXVuv2GarDV6PUJbktAKLXXckW1NU3I-0FXI8CBbcXhw3U45MatEWLyxrOk5; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFOBemdL8NY02r50o8WSIWd5NHD95QESh2ESoq7SoefWs4Dqcj6i--fi-zEiKnpi--ciKLhiKnRi--4iKL2iK.4i--fi-2fi-i2i--fi-i8iKnfi--ciKnpi-8hi--ciKnpi-8s; _T_WM=13862987552; XSRF-TOKEN=0db217; WEIBOCN_FROM=1110006030; MLOGIN=1',
    'Referer': 'https://m.weibo.cn/api/attitudes/show?id=4615677387998143&page=2',
    'pragma': 'no-cache',
    'referer': 'https://m.weibo.cn/sw.js',
}

params = (
    ('id', '4615677387998143'),
    ('page', '2'),
)

response = requests.get('https://m.weibo.cn/api/attitudes/show', headers=headers, params=params)
print(response.text)
