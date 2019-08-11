import urllib.request

try:
    #
    res = urllib.request.urlopen("http://www.baidu.com")
    print(res.read())
except urllib.request.URLError as e:
    print(e.reason)
