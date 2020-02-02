from wordcloud import WordCloud
import PIL .Image as image
import jieba
import numpy as np

def participle_word(text):
    text_list=jieba.cut(text)
    res=' '.join(text_list)
    return res

with open("D:\\githubMe\\flask-tutorial\\doc\\coronavirus_data.txt",'r', encoding='UTF-8') as fp:
    text=fp.read()
    text=participle_word(text)
    shade=np.array(image.open('D:\\githubMe\\flask-tutorial\\doc\\wordcloud2.png'))
    wordcloud=WordCloud(font_path="D:\\githubMe\\flask-tutorial\\doc\\msyh.ttc",width=800,height=800,mask=shade).generate(text)
    word_image=wordcloud.to_image()
    word_image.save('coronavirus_test_10.png','png')
