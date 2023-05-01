'''
Author: yanxiao333 yanxiao_333@126.com
Date: 2023-04-30 20:04:53
LastEditors: yanxiao333 yanxiao_333@126.com
LastEditTime: 2023-05-01 20:25:42
FilePath: \t2023_new_one\day5_428\3_js_七麦数据.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#!C:/Users/凡人/AppData/Local/Programs/Python/Python39/Python.exe
# -*- coding:UTF-8 -*-
# AUTHOR: XiaoDong Yan
# FILE: F:\vscode\t2023_new_one\day5_428\3_js_七麦数据.py
# DATE: 2023/04/30 周日
# TIME: 20:05:55

# DESCRIPTION:
from requests_html import HTMLSession
from copyheaders import headers_raw_to_dict
import execjs

url = 'https://api.qimai.cn/rank/indexPlus/brand_id/0?'
str = b'''
#'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8"
'Accept':"application/json, text/plain, */*"
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36
'''
session = HTMLSession()
headers = headers_raw_to_dict(str)


def main(params):
    try:
        res = session.get(url=url, headers=headers, params=params)
        if res.status_code == 200:
            print(res.encoding)
            res_html = res.json()
            print(res_html)

        else:
            return None
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    params = {
        'brand': 'all',
        'genre': '36',
        'device': 'iphone',
        'country': 'cn'
    }
    with open('./3.js', 'r', encoding='utf8') as f:
        js_read = f.read()
    ctx_encrypt = execjs.compile(js_read).call('url')
    params['analysis'] = ctx_encrypt
    # exit()
    print(params)
    main(params)
