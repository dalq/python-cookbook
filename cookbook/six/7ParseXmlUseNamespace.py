# 使用命名空间开解析XML文档
from xml.etree.ElementTree import parse


class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{' + uri + '}'

    def __call__(self, path):
        return path.format_map(self.namespaces)


ns = XMLNamespaces(html = 'http://www.w3.org/1999/xhtml')
doc = parse('./res/pred.xml')
text = doc.findtext(ns('content/{html}html/{html}head/{html}title'))
print(text)