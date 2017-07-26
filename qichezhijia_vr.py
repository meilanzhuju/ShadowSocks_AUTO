import requests

url = 'http://pano.autohome.com.cn/car/aa/mii/?pvareaid=100556'
res =requests.get(url)
print(res.status_code)
#print(res.content.decode('utf-8'))

url1 = 'https://pano.autohome.com.cn/car/aa/mii/?src=share'
res = requests.get(url1)
print(res.status_code)
print(res.content.decode('utf-8'))