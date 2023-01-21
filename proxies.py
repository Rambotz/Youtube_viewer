import aiohttp
import asyncio
import undetected_chromedriver as uc
import time
import requests


proxy = '159.223.14.199:443'
options = uc.ChromeOptions()
options.add_argument('--proxy-server=%s' % '104.37.101.17:8181')
driver = uc.Chrome(options=options)
status = ''
def check_proxy():
    try:
        r =  requests.get('https://httpbin.org/ip',proxies={'http':'104.37.101.17:8181'},timeout=5)
        print(r.json())

        driver.get('https://whatismyipaddress.com/')
        time.sleep(150)

    except:
        print('failed')
        pass

check_proxy()