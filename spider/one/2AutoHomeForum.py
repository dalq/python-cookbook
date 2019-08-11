import urllib.request
import json


class AutoHomeSpider:
    def __init__(self):
        self.sourceUrl = "https://club.autohome.com.cn/frontapi/topics/getByBbsId?pageindex=1&pagesize=50&bbs=c&bbsid=3462&fields=topicid,title,topicimgs&orderby=topicid-"
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

    def getPage(self):
        try:
            req = urllib.request.Request(self.sourceUrl, headers=self.header)
            res = urllib.request.urlopen(req)
            resStr = res.read().decode('utf-8')
            print(resStr)
            js = json.loads(resStr)
            print('共有{0}页、{1}条记录'.format(js['result']['pagecount'], js['result']['rowcount']))
        except urllib.request.URLError as e:
            print(e.reason)

    def start(self):
        page = self.getPage()


spider = AutoHomeSpider()
spider.start()