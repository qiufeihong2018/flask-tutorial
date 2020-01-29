# 1.15
import re
from urllib import request

class Spider():
    url='https://www.zhihu.com/special/all'
    root_pattern='<div class="SpecialListCard-infos">([\s\S]*?)</div>'
    title_pattern='<a class="SpecialListCard-title"></a>'
    number_pattern=''
    def __fetch_content(self):
        res=request.urlopen(Spider.url)
        htmls=res.read()
        htmls=str(htmls,encoding='utf-8')
        return htmls

    def __analysis(self,htmls):
        root_html=re.findall(Spider.root_pattern,htmls)
        anchors=[]
        for html in root_html:
            title=re.findall(Spider.title_pattern,html)
            number=re.findall()
        print(root_html[0])

    def go(self):
        htmls= self.__fetch_content()
        self.__analysis(htmls)

spider=Spider()
spider.go()