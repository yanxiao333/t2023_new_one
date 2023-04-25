'''
Author: yanxiao333 yanxiao_333@126.com
Date: 2023-04-23 21:04:22
LastEditors: yanxiao333 yanxiao_333@126.com
LastEditTime: 2023-04-25 19:41:56
FilePath: \t2023_new_one\js_spider_4_23.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

# -*- coding:UTF-8 -*-
# AUTHOR: XiaoDong Yan
# FILE: F:\vscode\t2023_new_one\js_spider_4_23.py
# DATE: 2023/04/23 周日
# TIME: 21:08:59

# DESCRIPTION:
from requests_html import HTMLSession
from copyheaders import headers_raw_to_dict

url = 'https://news.baidu.com/widget?id=LocalNews&ajax=json&t=1682422262523'

str = b'''
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36
X-Requested-With: XMLHttpRequest
'''

session = HTMLSession()
headers = headers_raw_to_dict(str)


def main():
    try:
        r = session.get(url=url, headers=headers)
        print(r.status_code, r.encoding)
        if r.status_code == 200:
            html_js = r.json()['data']['LocalNews']['data']['rows']
            print(html_js)
        else:
            return None
    except Exception as e:
        print('ERROR: %s' % str(e))


if __name__ == '__main__':
    main()
