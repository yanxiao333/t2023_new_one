import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    # 'Content-Type': 'application/json;charset=UTF-8',
    # 'Origin': 'https://ggzyfw.fj.gov.cn',
    # 'Pragma': 'no-cache',
    # 'Referer': 'https://ggzyfw.fj.gov.cn/business/list/',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'portal-sign': 'b795667b46d45e1d0b9e0c1fd7bba697',
    # 'sec-ch-ua':'"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'pageNo': 1,
    'pageSize': 20,
    'total': 3755,
    'AREACODE': '',
    'M_PROJECT_TYPE': '',
    'KIND': 'GCJS',
    'GGTYPE': '1',
    'PROTYPE': '',
    'timeType': '6',
    'BeginTime': '2022-10-25 00:00:00',
    'EndTime': '2023-04-25 23:59:59',
    'createTime': [],
    'ts': 1682390571792,
}

response = requests.post(
    'https://ggzyfw.fj.gov.cn/FwPortalApi/Trade/TradeInfo',
    headers=headers,
    json=json_data).json()['Data']
print(response)
