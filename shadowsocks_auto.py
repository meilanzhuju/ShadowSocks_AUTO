import requests
from bs4 import BeautifulSoup


url = 'http://www.autohome.com.cn/dealer/201404/10303815.html'
res = requests.get(url)

print(res.status_code)
#print(res.content)
res = res.content.decode('gbk')
#print(res)

soup = BeautifulSoup(res, 'html.parser')

print(soup.name)
print(soup.head.name)
print(soup.div['class'])
print(soup.title.text)
print(soup.title.string)   #有啥区别
text = soup.find(class_="article-text")
print(type(text))

print(text.children)

for child in text.children:
    print(child.string)


with open('./yutian.txt', 'w', encoding='utf-8') as f:
    for child in text.children:
        f.write(str(child.string))
    print(' saved OK!')

