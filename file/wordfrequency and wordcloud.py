#英文词频分析
import re
from collections import Counter

# 打开文件并读取内容
with open('A Sunrise on the Veld.txt', 'r', encoding='utf-8') as file1:
    text = file1.read().lower()
# 使用正则表达式找到所有的单词
words = re.findall(r'\b\w+\b', text)
# 使用Counter来计算每个单词的频率   ##########也可以不使用Counter，（看下面中文词频）即用words代替article/text来遍历
word_freq = Counter(words)
# 跳过stop_word_list中的词并打印出每个单词及其频率
swl=open('stop_word_list.txt','r',encoding='utf-8').read()
skip_swl=[]##创建空列表收集出现频率最高的前十个词
for word, freq in word_freq.items():
    if word not in swl:
        skip_swl.append(word)
        print(f'{word}: {freq}')


#中文词频分析
import jieba
#打开文件并读取内容,利用jieba进行中文词汇分割
with open('file1.txt','r',encoding='ansi') as file2:
    text2 = file2.read()
article=jieba.lcut(text2)
#遍历文件内容将每个词即词频存入词典
dicD={}
for word in article:
   if word not in dicD:
      dicD[word]=1
   else:
      dicD[word]+=1
#按照词频降序排列*******关于sorted(),lambda函数的应用很重要
D=sorted(list(dicD.items()),key=lambda lst:lst[1],reverse=True)
#跳过虚词并打印出词频
xuci=open('中文虚词列表.txt','r',encoding='ansi').read()
skip_xuci=[]##创建空列表收集出现频率最高的前十个词
for word,frequency in D:
    if word not in xuci:
        skip_xuci.append(word)
        print(f'{word}:{frequency}')
#第三方库wordcloud和词语可视化
import wordcloud
w=wordcloud.WordCloud(background_color='blue', #词云背景色，默认为黑
                      width=200, #宽
                      height=200, #高
                      max_font_size=80, #最大字号
                      max_words=10, #最多容纳的字数，默认为200
                      font_path='C:/Windows/Fonts/simhei.ttf')
code=input()
if code=='D':
    txt=skip_xuci
    w.generate( str(txt[:9]) )  ##将文本生成词云(仅读字符串）
    w.to_file( 'D:/test.png' )  ##将次云保存为图像文件
elif code=='E':
    txt=skip_swl
    w.generate( str(txt[:9]) )  ##将文本生成词云(只读字符串）
    w.to_file( 'D:/test.png' )  ##将次云保存为图像文件
else:
    print("代号错误")







