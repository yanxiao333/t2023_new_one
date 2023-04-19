import requests
import execjs

cookies = {
    'btoken': 'JCWHXWQHVF2F7OEBJSZSMI2H17JM24B2',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1681907404',
    'hy_data_2020_id':
    '187997e4cf8bed-0c04ca5b95d0bc-26031b51-1296000-187997e4cf9d25',
    'hy_data_2020_js_sdk':
    '%7B%22distinct_id%22%3A%22187997e4cf8bed-0c04ca5b95d0bc-26031b51-1296000-187997e4cf9d25%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22187997e4cf8bed-0c04ca5b95d0bc-26031b51-1296000-187997e4cf9d25%22%7D',
    'sajssdk_2020_cross_new_user': '1',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1681908525',
}

headers = {
    'authority':
    'www.xiniudata.com',
    'accept':
    'application/json',
    'accept-language':
    'zh-CN,zh;q=0.9',
    'content-type':
    'application/json',
    # 'cookie': 'btoken=JCWHXWQHVF2F7OEBJSZSMI2H17JM24B2; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1681907404; hy_data_2020_id=187997e4cf8bed-0c04ca5b95d0bc-26031b51-1296000-187997e4cf9d25; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%22187997e4cf8bed-0c04ca5b95d0bc-26031b51-1296000-187997e4cf9d25%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22187997e4cf8bed-0c04ca5b95d0bc-26031b51-1296000-187997e4cf9d25%22%7D; sajssdk_2020_cross_new_user=1; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1681908525',
    'origin':
    'https://www.xiniudata.com',
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
    'payload': 'LBc3V0I6ZGB5bXsxTCQnPRBuBAQVcDhbICcmb2x3AjI=',
    'sig': 'CE704F132C4E47B31E91773020275904',
    'v': 1,
}

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
text1 = response['d']
# print(response)
jscode1 = open('./demo1.js', 'r', encoding='utf-8').read()
datas = execjs.compile(jscode1).call('main456', text1)
# print(datas['list'])
for i in datas['list']:
    print(i['name'], i['event'])
