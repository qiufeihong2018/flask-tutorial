import re
from urllib import request

class Spider():
    url='https://www.zhihu.com/special/all'
    root_pattern='<div class="SpecialListCard-infos">([\s\S]*?)</div>'
    # href里面的随机值
    title_pattern='<a href="/special/[\s\S]*?" class="SpecialListCard-title" data-za-detail-view-id="5814">([\s\S]*?)</a>'
    number_pattern='<span>([\s\S]*?)</span>'

    # 抓取数据
    def __fetch_content(self):
        res=request.urlopen(Spider.url)
        htmls=res.read()
        htmls=str(htmls,encoding='utf-8')
        return htmls
    
    # 清洗数据
    def __analysis(self,htmls):
        root_html=re.findall(Spider.root_pattern,htmls)
        anchors=[]
        for html in root_html:
            dict={'number':0,'title':0}
            number=re.findall(Spider.number_pattern,html)
            number=number[1].split('<')[0]
            number=re.sub('[,]','',number)
            title=re.findall(Spider.title_pattern,html)
            title=title[0]
            # 去除\r\n\t字符
            title=re.sub('[\r\n\t]', '', title)
            dict['number']=number
            dict['title']=title
            anchors.append(dict)
        return anchors

    # 排序 
    def __sort(self,anchors):
        anchors.sort(key=lambda x:int(x['number']),reverse=True)
        return anchors

    def main(self):
        htmls= self.__fetch_content()
        anchors=self.__analysis(htmls)
        result=self.__sort(anchors)
        print(result)

spider=Spider()
spider.main()
# [{'number': '109062365', 'title': '新华社 X 知乎 联合关注：武汉，加油！'}, {'number': '34503496', 'title': '科比意外离世，你对他有哪些回忆？'}, {'number': '31640616', 'title': '双腿不能带你去的地方，电影
# 带你去'}, {'number': '23971587', 'title': '医疗：如何防治新型肺炎，这些你必须知道'}, {'number': '18007944', 'title': '春节「纪录片」'}, {'number': '13496649', 'title': '回家「路」上'}, {'number': '9745747', 'title': '原地宅住，认真追剧'}, {'number': '5695005', 'title': '「奇幻爱情」想见你'}, {'number': '1823305', 'title': '新华社 X 知乎联合辟谣：这些关于新型肺炎的消息，都是假的'}, {'number': '1042558', 'title': '春节宅家，不如教会爸妈用手机'}]