import requests as req
import time as ti
import random as rand

URL = 'https://www.luogu.com.cn/paintBoard/paint'
COOKIES = [
    dict(_uid='', __client_id='')
]
USER_AGENT = 'LuoguPainter/1.0 Python/3.8.7'
MAXX = 1000
MAXY = 600
headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.luogu.com.cn',
    'referer': 'https://www.luogu.com.cn/paintBoard',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': USER_AGENT,
    'x-requested-with': 'XMLHttpRequest'
}

colors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
          16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

while True:
    form_data = {
        'x': int(rand.random() * MAXX),
        'y': int(rand.random() * MAXY),
        'color': colors[int(rand.random() * 32)]
    }
    for c in COOKIES:
        r = req.post(URL, form_data, headers=headers, cookies=c)
        if r.status_code == 200:
            print(form_data, 'by uid =', c['_uid'])
        else:
            print('[ERR]', form_data, 'by uid =',
                  c['_uid'], 'status_code =', r.status_code)
            print(r.content.decode('utf-8', 'strict'))
    ti.sleep(30)
