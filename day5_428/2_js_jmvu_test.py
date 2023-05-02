'''
Author: yanxiao333 yanxiao_333@126.com
Date: 2023-04-29 20:01:43
LastEditors: yanxiao333 yanxiao_333@126.com
LastEditTime: 2023-05-02 15:54:47
FilePath: \t2023_new_one\day5_428\2_js_jmvu_test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#C:/Users/凡人/AppData/Local/Programs/Python/Python39/Python.exe
# -*- coding:UTF-8 -*-
# AUTHOR: XiaoDong Yan
# FILE: F:\vscode\t2023_new_one\day5_428\2_js_jmvu_test.py
# DATE: 2023/04/29 周六
# TIME: 20:01:58

# DESCRIPTION:
import requests
import execjs
import json

cookies = {
    'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c': '1682764250',
    'Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c': '1682767171',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1682764250; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1682767171',
    'Referer': 'https://jzsc.mohurd.gov.cn/data/company',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'accessToken': '',
    'sec-ch-ua':
    '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'timeout': '30000',
}


def main(params):
    response = requests.get(
        'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list',
        # 'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/staff/list'
        params=params,
        cookies=cookies,
        headers=headers,
    ).text
    return response
    # print(response)


if __name__ == '__main__':
    for page in range(1, 10):
        params = {
            'pg': page,
            'pgsz': '15',
            'total': '0',
        }
        response = main(params)
        with open('./2.js', 'r', encoding='utf-8') as f:
            js_encrypt = f.read()
        #运行js文件
        ctx_encrypt = execjs.compile(js_encrypt)
        #调用函数，传递参数data
        datas = ctx_encrypt.call('h', response)
        json_data = json.loads(datas)['data']['list']
        for i in json_data:
            print(i)