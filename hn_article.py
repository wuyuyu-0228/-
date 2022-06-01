import requests

#执行API调用并且存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print(f"Status code:{r.status_code}")