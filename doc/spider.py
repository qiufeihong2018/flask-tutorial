import re
from urllib import request

class Spider():
    url='https://www.zhihu.com/special/all'
    root_pattern='<div class="SpecialListCard-infos">([\s\S]*?)</div>'
    # href里面的随机值
    title_pattern='<a href="/special/[\s\S]*?" class="SpecialListCard-title" data-za-detail-view-id="5814">([\s\S]*?)</a>'
    number_pattern='<span>([\s\S]*?)</span>'
    def __fetch_content(self):
        res=request.urlopen(Spider.url)
        htmls=res.read()
        htmls=str(htmls,encoding='utf-8')
        return htmls

    def __analysis(self,htmls):
        root_html=re.findall(Spider.root_pattern,htmls)
        anchors=[]
        for html in root_html:
            dict={'number':0,'title':0}
            number=re.findall(Spider.number_pattern,html)
            number=number[1].split('<')[0]
            title=re.findall(Spider.title_pattern,html)
            title=title[0]
            dict['number']=number
            dict['title']=title
            anchors.append(dict)
        return anchors


    def __sort(self,anchors):
        result=[]
        for item in anchors:
            print(item)
        # return result
        
    def go(self):
        htmls= self.__fetch_content()
        anchors=self.__analysis(htmls)
        result=self.__sort(anchors)

spider=Spider()
spider.go()