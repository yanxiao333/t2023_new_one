import requests
import execjs
cookies = {
    'btoken': 'CH9L2VLN61YXDI796H34UQIWDDII9CC1',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1681882069',
    'hy_data_2020_id': '18797fbb72a482-02e2014d56ccf5-26031b51-1440000-18797fbb72b995',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%2218797fbb72a482-02e2014d56ccf5-26031b51-1440000-18797fbb72b995%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218797fbb72a482-02e2014d56ccf5-26031b51-1440000-18797fbb72b995%22%7D',
    'sajssdk_2020_cross_new_user': '1',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1681882182',
}

headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'btoken=CH9L2VLN61YXDI796H34UQIWDDII9CC1; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1681882069; hy_data_2020_id=18797fbb72a482-02e2014d56ccf5-26031b51-1440000-18797fbb72b995; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%2218797fbb72a482-02e2014d56ccf5-26031b51-1440000-18797fbb72b995%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218797fbb72a482-02e2014d56ccf5-26031b51-1440000-18797fbb72b995%22%7D; sajssdk_2020_cross_new_user=1; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1681882182',
    'origin': 'https://www.xiniudata.com',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}
jscode = open('./play123.js', 'r', encoding='utf8').read()
params = execjs.compile(jscode).call('main123')
print(params)
# 加密参数逆向

json_data = {
    'payload': params['payload'],
    'sig': params['sig'],
    'v': 1,
}
'''
JSON.stringify(l.payload)
Object(c.d)(JSON.stringify(l.payload))
Object(c.c)(Object(c.d)(JSON.stringify(l.payload)))
'''

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
print(response)
