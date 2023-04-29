import json

import requests
import execjs

headers = {
    'Accept':
    'application/json, text/plain, */*',
    'Content-Type':
    'application/x-www-form-urlencoded',
    'Origin':
    'https://www.qimingpian.com',
    'Referer':
    'https://www.qimingpian.com/finosda/project/pinvestment',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
}

data = {
    'time_interval': '',
    'tag': '',
    'tag_type': '',
    'province': '',
    'lunci': '',
    'page': 2,
    'num': 20,
    'unionid': '',
}


def get_encry_data():
    url = 'https://vipapi.qimingpian.com/DataList/productListVip'
    res = requests.post(url, data=data, headers=headers)
    print(res.json())
    return res.json()['encrypt_data']


if __name__ == '__main__':
    encrypt_data = get_encry_data()
    with open('1.js', 'r', encoding='utf-8') as f:
        s = f.read()
    result = execjs.compile(s).call('s', encrypt_data)
    # print(result)
    js_data = json.loads(result)
    print(js_data)
