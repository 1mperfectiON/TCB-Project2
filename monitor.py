import requests
from bs4 import BeautifulSoup
import lxml
import time
from dhooks import Webhook
import random
import send_webhook

proxy_pool=[
    {
        "http":"http://Z4y2Td9x!a5:pas1SxHC@snkrs-us-S138.chicooked.io:33128",
        "https":"http://Z4y2Td9x!a5:pas1SxHC@snkrs-us-S138.chicooked.io:33128",
    },
    {
        "http":"Z4y2Td9x!a1:pas1SxHC@snkrs-us-S86.chicooked.io:33128",
        "https":"Z4y2Td9x!a1:pas1SxHC@snkrs-us-S86.chicooked.io:33128",
    },
    {
        "http": "Z4y2Td9x!a1:pas1SxHC@snkrs-us-S308.chicooked.io:33128",
        "https": "Z4y2Td9x!a1:pas1SxHC@snkrs-us-S308.chicooked.io:33128",
    },
    {
        "http": "Z4y2Td9x!a5:pas1SxHC@snkrs-us-S2.chicooked.io:33128",
        "https": "Z4y2Td9x!a5:pas1SxHC@snkrs-us-S2.chicooked.io:33128",
    },
    {
        "http": "Z4y2Td9x!a2:pas1SxHC@snkrs-us-S9.chicooked.io:33128",
        "https": "Z4y2Td9x!a2:pas1SxHC@snkrs-us-S9.chicooked.io:33128",
    }
]


def get_data():
    url="https://kith.com/collections/kith-monday-program/products/kith-mosaic-tee-slate"
    cookies = {
        'snize_session': 'qqknrw72k',
        '__cfduid': 'd63808aa7b9335ae70fcbdf38e3edf9c71591173984',
        '_y': '480aaccf-6363-4337-96bb-a51de08250d8',
        'cart_currency': 'USD',
        '_orig_referrer': 'https%3A%2F%2Fwww.google.com%2F',
        'secure_customer_sig': '',
        '_landing_page': '%2Fcollections%2Fmens-footwear',
        '_shopify_y': '480aaccf-6363-4337-96bb-a51de08250d8',
        '_shopify_fs': '2020-06-03T08%3A46%3A25.289Z',
        '_ga': 'GA1.2.2106668635.1591173986',
        '_gid': 'GA1.2.1392446020.1591173986',
        'GlobalE_Data': '%7B%22countryISO%22%3A%22US%22%2C%22currencyCode%22%3A%22USD%22%2C%22cultureCode%22%3A%22en-US%22%7D',
        '_fbp': 'fb.1.1591173987487.1323959225',
        'cart_sig': '',
        'cart': '3428dc3692352a2bfc99ed2f798c2de5',
        'cart_ts': '1591173993',
        'snize-recommendation': 'abnjr2gpzpq',
        'snize_uid': '963u0fl4g',
        'KL_FORMS_MODAL': '{%22disabledForms%22:{%22KyEV5m%22:{%22lastCloseTime%22:1591174012%2C%22successActionTypes%22:[]}}%2C%22viewedForms%22:{%22KyEV5m%22:281307}}',
        'acceptedCookies': 'yes',
        'shopify_pay_redirect': 'pending',
        '_s': '80e0b182-2073-4511-73A6-7B7B0BEC362D',
        '_shopify_s': '80e0b182-2073-4511-73A6-7B7B0BEC362D',
        '_gat_gtag_UA_62344036_3': '1',
        '_shopify_sa_t': '2020-06-04T19%3A48%3A26.800Z',
        '_shopify_sa_p': '',
        '_gat': '1',
        '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE1OTExNzM5ODgsInZhbHVlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly9raXRoLmNvbS9jb2xsZWN0aW9ucy9tZW5zLWZvb3R3ZWFyIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNTkxMzAwMTExLCJ2YWx1ZSI6Imh0dHBzOi8va2l0aC5jb20vY29sbGVjdGlvbnMvbWVucy1mb290d2VhciIsImZpcnN0X3BhZ2UiOiJodHRwczovL2tpdGguY29tL2NvbGxlY3Rpb25zL21lbnMtZm9vdHdlYXIvcHJvZHVjdHMvbmV3LWJhbGFuY2UtbTk5Ni1ncmV5In19',
        'arp_scroll_position': '0',
    }

    headers = {
        'authority': 'kith.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
        'if-none-match': 'cacheable:b733eb9b4a0237aeb8ef8e0877a12bd8',
    }

    kith_data=requests.get(url,proxies=random.choice(proxy_pool),headers=headers,cookies=cookies).text

    soup=BeautifulSoup(kith_data,"lxml")

    stock_level=soup.find_all("link",itemprop="availability")
    return str(stock_level)


data1="[<link href=\"http://schema.org/OutOfStock\" itemprop=\"availability\"/>]"
while True:
    data2=get_data()
    if data1!=data2:
        send_webhook.SendOutWebhook()
        break
    else:
        time.sleep(1)
        print("Sleep for 1 seconds.")





