# bin/python310

from requests_html import HTMLSession
from copyheaders import headers_raw_to_dict
from gne import GeneralNewsExtractor

url = 'https://www.msn.cn/zh-cn/news/redstarnews?ocid=BHEA000&cvid=f14e433625d645f8a49c3143b89aab09&ei=5'
str = b'''
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36
'''
session = HTMLSession()
headers = headers_raw_to_dict(str)
extractor = GeneralNewsExtractor()


def main():
    res = session.get(url=url, headers=headers)
    print(res.status_code, res.encoding)
    if res.status_code == 200:
        # print(res.text)
        details = res.html.find('.rc-container-js .list li a')
        # print(details)
        for data1 in details:
            detail = data1.attrs['aria-label']
            detail_url = 'https://www.msn.cn'+data1.attrs['href']
            # print(detail, detail_url)
        return detail_url
    else:
        return None


def get_download_content(detail_url):
    try:
        res1 = session.get(url=detail_url, headers=headers)
        print(res1.status_code, res1.encoding)
        if res1.status_code == 200:
            html = res1.text
            print(html)
            exit()
            content = extractor.extract(html)
            print(content)
        pass
    except Exception as e:
        print('Error downloading', e)


if __name__ == '__main__':
    detail_url = main()
    get_download_content(detail_url)
