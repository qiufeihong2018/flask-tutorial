from wordcloud import WordCloud
import PIL .Image as image

with open("D:\Coronavirus.txt") as fp:
    text=fp.read()
    wordcloud=WordCloud().generate(text)
    word_image=wordcloud.to_image()
    word_image.save('Coronavirus.png','png')