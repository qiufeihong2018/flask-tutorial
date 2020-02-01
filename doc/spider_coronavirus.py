import re
from urllib import request

class Spider():
    url='https://ncov.dxy.cn/ncovh5/view/pneumonia_peopleapp?from=timeline&isappinstalled=0'
    
    # 抓取数据
    def fetch_content(self):
        res=request.urlopen(Spider.url)
        htmls=res.read()
        htmls=str(htmls,encoding='utf-8')
        return htmls
    # 解析数据
    def parse_content(self,htmls):
        pattern='<script id="[\s\S]*?">([\s\S]*?)</script>'
        htmls=re.findall(pattern,htmls)
        list=[]
        for dict_item in htmls:
            dict={}
            dict_list=dict_item.split('=')
            if 'window.' in dict_list[0]:
                json_key=dict_list[0].split('window.')[1].strip()
            if '}catch' in dict_list[1]:
                json_val=dict_list[1].split('}catch')[0].strip()
            dict[json_key]=json_val
            # print(dict)
            list.append(dict)
        return list
    # 保存数据
    def write_content(self,list):
        file=open('coronavirus_data.json','w', encoding='UTF-8')
        file.write(str(list))
        file.close()

    def main(self):
        htmls= self.fetch_content()
        list=self.parse_content(htmls)
        self.write_content(list)
        # print(htmls)

spider=Spider()
spider.main()