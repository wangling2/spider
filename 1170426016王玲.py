def function_name(panams):
    res = re.search("(.jpg|.JPG|.gif|.GIF|)$",url)
import urllib.request
import urllib.parse
data = urllib.parse.urlencode({'wd':'呵呵'},encoding='utf8')
print(data)
ur1='http://www.baidu.com/s?'+data
print(ur1)
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)

data = bytes(urllib.parse.urlencode({'pw':'652','un':'281'}),enconding='utf8')
url = 'http://httpbin.org/post'
response = urllib.request.urlopen(url,data=data)
print(result)
