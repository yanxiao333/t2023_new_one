#!/usr/bin/python3
import requests, re
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
    res.encoding = '4'
    html_data = res.text
    # print(html_data)
    return html_data


def get_response_data(html_data):
    '''
    解析函数：
    '''
    html_data1 = html_data.replace('<record><', '').replace(
        '![CDATA[',
        '').replace(']]></record>',
                    '').replace('<datastore>',
                                '').replace('nextgroup><',
                                            '').replace('</datastore>', '')
    # print(html_data1)
    # 我们获取标题
    detail_dat = re.findall(
        f'<li>.*?<a target="_blank" href="(.*?)" title="(.*?)</a>.*?</li>',
        html_data1)
    # print(detail_dat)
    return detail_dat


def reparse_detail_dat(detail_dat):
    for data2 in detail_dat:
        if '://' not in data2[0]:
            link = 'http://longxian.gov.cn' + data2[0]
            title = data2[1]
            print(link, title)


def main():
    '''
    主函数体
    '''
    html_data = run()
    detail_dat = get_response_data(html_data)
    reparse_detail_dat(detail_dat)


if __name__ == '__main__':
    main()
