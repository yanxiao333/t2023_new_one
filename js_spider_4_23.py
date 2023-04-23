#!C:/Users/凡人/AppData/Local/Programs/Python/Python39/Python.exe
# -*- coding:UTF-8 -*-
# AUTHOR: XiaoDong Yan
# FILE: F:\vscode\t2023_new_one\js_spider_4_23.py
# DATE: 2023/04/23 周日
# TIME: 21:08:59

# DESCRIPTION:
from requests_html import HTMLSession
from copyheaders import headers_raw_to_dict

url = ''
str = b'''

'''

session = HTMLSession()
headers = headers_raw_to_dict(str)


def main():
    try:
        r = session.get(url=url, headers=headers)
        print(r.status_code, r.encoding)

        pass
    except Exception as e:
        print('ERROR: %s' % str(e))


if __name__ == '__main__':
    main()