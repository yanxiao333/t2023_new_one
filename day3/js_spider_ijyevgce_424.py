import requests
import execjs

parame = execjs.compile(open('./day3_demo.js', 'r',
                        encoding='utf8').read()).call('main123')
# print(parame['data'])
cookies = {
    'JSESSIONID': 'A37FCBC4B7F24783227ADF2EE1216782',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/octet-stream',
    # 'Cookie': 'JSESSIONID=A37FCBC4B7F24783227ADF2EE1216782',
    'Origin': 'http://www.spolicy.com',
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

# data = '\n\x016\x12\x00\x1a\x00"\x00*\x002\x008\x00@\x01H\aP\x01'

response = requests.post(
    'http://www.spolicy.com/info_api/policyType/showPolicyType',
    cookies=cookies,
    headers=headers,
    data=bytes(parame['data']),
    verify=False,
).json()['data']['rows']
for res in response:
    print(res)
