import requests
import re

with open("proxy.txt", "w") as f:
    for page in range(1, 17):
        url = f'https://proxylist.geonode.com/api/proxy-list?limit=500&page={page}&sort_by=lastChecked&sort_type=desc&speed=fast'
        response = requests.get(url)
        data = response.json()
        
        for proxy in data['data']:
            ip = proxy['ip']
            ports = re.findall(r'\d+', proxy['port'])
            for port in ports:
                proxy_string = ip + ":" + port
                f.write(proxy_string+'\n')
