import requests

str_ = open('res3.txt'，"rb").read()
results = res3.findall('http://www.baidu.com/s?')
with open("urls.txt","wb")as f:
    f.write("\r\n".joint(results))


url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
res = requests.get(url)
HTML = res.text
ars = HTML.split('\n')
    for url in ars:
        name = url.split('/')[-1]
        response = requests.get(url)
        content = response.content
    with open(name,'wb')as f:
            f.write(content)