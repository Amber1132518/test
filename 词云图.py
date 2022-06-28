
import pickle
from os import path
import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
with open('F:\\互联网+\\流浪动物.txt', 'r', encoding='utf-8') as fin:
    text = fin.read()
backgroud_Image = plt.imread('F:\\互联网+\\宠物图片.jpeg')
print('加载图片成功！')
'''设置词云样式'''
wc = WordCloud(background_color='white',mask=backgroud_Image,font_path='msyh.ttc',max_words=2000,stopwords=STOPWORDS,max_font_size=150,random_state=30)
wc.generate_from_text(text)
print('开始加载文本')
plt.imshow(wc)
plt.axis('off')
plt.show()
d = path.dirname(__file__)
wc.to_file(path.join(d, "词云图.jpg"))
print('生成词云成功!')
# 用matplotlib渲染出词云图
# 调整画布的长和宽
#plt.subplots(figsize=(12,8))
#plt.imshow(word_cloud)
#plt.axis("off")