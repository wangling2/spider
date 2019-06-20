import urllib.request
proxy_handle = {'http':'http://1.198.73.189 '}
proxy = urllib.request.ProxyHandler(proxy_handle)
opener = urllib.request.build_opener(proxy)
response = opener.open(url)


import http.cookiejar,urllib.request
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1614.400'}
cookie = http.cookiejar.MozillaCookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
url = 'http://www.baidu.com'
request = urllib.request.Request(url,headers=headers)
response = opener.open(request)
for item in cookie:
    print(item.name,item.value)
    filename = 'qaz.txt'
    cookie.save(filename=filename,ignore_discard=True,ignore_expires=True)
    cookie = http.cookiejar.MozillaCookieJar()
    cookie.load('qazr.txt')
    print(cookie)
