#!C:/Programs/Python/Python310/python.exe
# -*- coding:UTF-8 -*-
# AUTHOR: XiaoDong Yan
# FILE: E:\vscode_items\t2023_new_one\js_spider_ijyevgce_4241.py
# DATE: 2023/04/24 周一
# TIME: 15:51:54

# DESCRIPTION:

import requests
import execjs

cookies = {
    'btoken': 'CH9L2VLN61YXDI796H34UQIWDDII9CC1',
    'hy_data_2020_id':
    '18797fbb72a482-02e2014d56ccf5-26031b51-1440000-18797fbb72b995',
    'hy_data_2020_js_sdk':
    '%7B%22distinct_id%22%3A%2218797fbb72a482-02e2014d56ccf5-26031b51-1440000-18797fbb72b995%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218797fbb72a482-02e2014d56ccf5-26031b51-1440000-18797fbb72b995%22%7D',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1681882069,1682325562',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1682325588',
}

headers = {
    'authority':
    'www.xiniudata.com',
    'accept':
    'application/json',
    'accept-language':
    'zh-CN,zh;q=0.9',
    'cache-control':
    'no-cache',
    'content-type':
    'application/json',
    # 'cookie': 'btoken=CH9L2VLN61YXDI796H34UQIWDDII9CC1; hy_data_2020_id=18797fbb72a482-02e2014d56ccf5-26031b51-1440000-18797fbb72b995; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%2218797fbb72a482-02e2014d56ccf5-26031b51-1440000-18797fbb72b995%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218797fbb72a482-02e2014d56ccf5-26031b51-1440000-18797fbb72b995%22%7D; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1681882069,1682325562; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1682325588',
    'origin':
    'https://www.xiniudata.com',
    'pragma':
    'no-cache',
    'referer':
    'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua':
    '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile':
    '?0',
    'sec-ch-ua-platform':
    '"Windows"',
    'sec-fetch-dest':
    'empty',
    'sec-fetch-mode':
    'cors',
    'sec-fetch-site':
    'same-origin',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

json_data = {
    'payload': 'LBc3V0I6ZGB6bXsxTCQnPRBuBhgbPj1fJDpwd2R1Tw==',
    'sig': '49AF9D32DA6AA7E5B32214EC011FE0B7',
    'v': 1,
}

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
text1 = response['d']
jscode1 = open('js_day2_demo.js', 'r', encoding='utf8').read()
datas = execjs.compile(jscode1).call('main345', text1)['list']
for i in datas:
    print(i['name'], i['event'])
