import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://ggzyfw.fj.gov.cn',
    'Referer': 'https://ggzyfw.fj.gov.cn/business/list/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'portal-sign': '415e35a0224bd0c0835e0bf8fc880ccf',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'pageNo': 1,
    'pageSize': 20,
    'total': 0,
    'AREACODE': '',
    'M_PROJECT_TYPE': '',
    'KIND': 'GCJS',
    'GGTYPE': '1',
    'PROTYPE': '',
    'timeType': '6',
    'BeginTime': '2022-10-20 00:00:00',
    'EndTime': '2023-04-20 23:59:59',
    'createTime': [],
    'ts': 1681965734082,
}

response = requests.post(
    'https://ggzyfw.fj.gov.cn/FwPortalApi/Trade/TradeInfo', headers=headers, json=json_data).json()
print(response)
