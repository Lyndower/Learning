import wordcloud
import jieba

def word_analysis(filename,flag):
    f = open(filename, encoding='utf-8')
    speech_text = f.read()
    f.close()

##对于读取文本文件的选择
    if flag == 'E':
        speech = speech_text.lower().split()
    else:
        speech = jieba.lcut(speech_text)

#遍历文本内容收集词及计算词频
    dic = {}
    for word in speech:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
#按词频降序排列
    swd = sorted(list(dic.items()), key=lambda lst: lst[1], reverse=True)

##对于跳过词文件的选择
    if flag == 'E':
        f1 = open('stop_word_list.txt')
    else:
        f1 = open('中文虚词列表.txt')
    stop_wds = f1.read()
    f1.close()
#跳过一些指定的词
    s = ''
    count = 0
    for kword, times in swd:
        if kword not in stop_wds and count < 10:
            s += kword + ' '
            count += 1
            # print(kword,times)

    return s

#词云分析和词语可视化
def word_cloud(filename, s):
    w = wordcloud.WordCloud(
        background_color='white',
        width=150,
        height=120,
        max_font_size=48,
        min_font_size=5,
        font_path='C:/Windows/Fonts/Deng.ttf'
    )
    w.generate(s)
    w.to_file('%s.png'%filename[:-4])
    print('已生成词云图片：%s.png'%filename[:-4])
#选择词云化的文件词语
while 1:
    flag = input('请输入字母E或C，输入Q退出')
    if flag.upper() == 'Q':
        break
    if flag == 'E':
        filename = '英文素材.txt'
    elif flag == 'C':
        filename = '中文素材.txt'
    else:
        print('输入有误')
        continue
    s = word_analysis(filename, flag)
    word_cloud(filename, s)
