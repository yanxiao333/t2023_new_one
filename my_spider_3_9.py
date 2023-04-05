#!/usr/bin/python3
import requests
from copyheaders import headers_raw_to_dict
from pyquery import PyQuery as pq

url = 'http://longxian.gov.cn/col/col4227/index.html'
str = b'''
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36
'''
headers = headers_raw_to_dict(str)


def run():
    res = requests.get(url=url, headers=headers)
    print(res.status_code, res.encoding)
    res.encoding = 'gb2312'
    html_data = res.text
    # print(html_data)
    return html_data


def get_response_data(html_data):
    '''
    解析函数：
    '''
    html_data1 = html_data.replace('')
    doc = pq(html_data)
    # 我们获取标题
    title_data = doc('#13861 .simple_pgContainer li')
    print(title_data)


def main():
    '''
    主函数体
    '''
    html_data = run()
    get_response_data(html_data)


if __name__ == '__main__':
    main()
