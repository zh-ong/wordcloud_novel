#coding:utf-8
import sys
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from scipy.misc import imread
from datetime import datetime

jieba.add_word('路西恩')
jieba.add_word('恐怖如斯')

def customfilter(segs):
	filter=open('filter.txt').read()
	resseg=""
	for seg in segs:
		if seg not in filter:
			resseg+=' '+seg
	return resseg

novel=sys.argv[1] #'assz.txt'
imgmask=sys.argv[2] #'assz.jpg'
t=datetime.now()
resimg="word_"+novel.split('.')[0]+"_"+str(t.month)+str(t.day)+str(t.hour)+str(t.minute)+str(t.second)+".jpg"

novletext=open(novel).read()
hmseg=jieba.cut(novletext)

seg_space=customfilter(hmseg)

alice_color=imread(imgmask)

fwc=WordCloud(font_path='msyh.ttc',max_words=1000,background_color='white',mask=alice_color,max_font_size=100,font_step=1).generate(seg_space)
imagecolor=ImageColorGenerator(alice_color)
plt.imshow(fwc.recolor(color_func=imagecolor))
plt.axis("off")
plt.show()
fwc.to_file(resimg)