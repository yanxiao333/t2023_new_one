
# -*- coding:UTF-8 -*-
# AUTHOR: XiaoDong Yan
# FILE: E:\vscode_items\t2023_new_one\day4\js_427_13.py
# DATE: 2023/04/27 周四
# TIME: 14:00:08

# DESCRIPTION:
import requests
import execjs

cookies = {
    'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c': '1682573348',
    'Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c': '1682574769',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1682573348; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1682574769',
    'Pragma': 'no-cache',
    'Referer': 'https://jzsc.mohurd.gov.cn/data/company',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'accessToken': '',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'timeout': '30000',
}

params = {
    'pg': '1',
    'pgsz': '15',
    'total': '450',
}

response = requests.get(
    'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list',
    params=params,
    cookies=cookies,
    headers=headers,
)

if response.status_code == 200:
    html_content = response.text
    print(html_content)
    jscode = open('./js_427_13.js', 'r', encoding='utf8').read()
    ctx = execjs.compile(jscode).call('h', html_content)
    print(ctx)
else:
    pass
