from wordcloud import WordCloud
import PIL .Image as image
import jieba
import numpy as np

def __translate_zh(text):
    text_list=jieba.cut(text)
    res=' '.join(text_list)
    return res

with open("D:\\githubMe\\flask-tutorial\\doc\\coronavirus_data.json",'r', encoding='UTF-8') as fp:
# with open("D:\\githubMe\\flask-tutorial\\doc\\Coronavirus_2.txt",'r', encoding='UTF-8') as fp:
    text=fp.read()
    text=__translate_zh(text)
    # shade=np.array(image.open('D:\\githubMe\\flask-tutorial\\doc\\Coronavirus9.png'))
    # wordcloud=WordCloud(mask=shade,font_path="D:\\githubMe\\flask-tutorial\\doc\\msyh.ttc").generate(text)
    wordcloud=WordCloud(font_path="D:\\githubMe\\flask-tutorial\\doc\\msyh.ttc").generate(text)
    word_image=wordcloud.to_image()
    word_image.save('Coronavirus_test_5.png','png')



