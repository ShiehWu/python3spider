# -*- coding: utf-8 -*-
"""
    :author: Wu Xie (吴谢)
    :url: http://hellowuxie.com
    :copyright: © 2018 Wu Xie <shiehng@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from urllib.parse import urlencode
import requests
import math

base_url = "https://www.panda.tv/live_lists?"

headers = {
    'Host': 'www.panda.tv',
    'Referer': 'https://www.panda.tv/all',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/65.0.3325.181 Safari/537.36',
    'X-Requests-With': 'XMLhttpRequest',
}


def get_total():
    params = {
        'status': '2',
        'token': '',
        'pageno': '1',
        'pagenum': '120',
        'order': 'top',
        '_': '1529156676586'
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            total = response.json().get('data').get('total')
            return total
    except requests.ConnectionError as e:
        print("Error", e.args)


def get_page(page):
    params = {
        'status': '2',
        'token': '',
        'pageno': page,
        'pagenum': '120',
        'order': 'top',
        '_': '1529156676586'
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print("Error", e.args)


def parse_page(json):
    if json:
        items = json.get('data').get('items')
        for item in items:
            live = {}
            live['live_name'] = item.get('name')
            live['live_id'] = item.get('id')
            live['views'] = item.get('person_num')
            live['nick_name'] = item.get('userinfo').get('nickName')
            live['live_class'] = item.get('classification').get('cname')
            yield live


if __name__ == '__main__':
    total = get_total()
    pages = math.ceil(total / 120)
    file = open('results.txt', 'w', encoding='utf-8')
    for page in range(1, pages):
        print('Touching %d page' % page)
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result, file=file)
    file.close()
