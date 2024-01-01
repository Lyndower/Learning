#1 read()
f=open('file1.txt','r',encoding='ANSI')
l1=f.read().split('\n') #read()默认读全篇，可加(size);无换行符，输出字符串，用split()将其转为列表并按一定分隔符分隔成不同字符串元素，如f.read().split('\n')
print(l1)
sum1=0
for line in l1: #滤掉了换行符'\n'
    sum1+=len(line)
print('总行数%d,总字符%d'%(len(l1),sum1))

#2 readlines()
f.seek(0)
l2=f.readlines() #换行和空格转义符会输出，以每行为字符串元素在列表中输出
print(l2)
sum2=0
for line in l2:
    sum2+=len(line)
print('总行数%d,总字符%d'%(len(l2),sum2))

#3.1 readline()
f.seek(0)
line=f.readline() ##先在循环前read一次，创一个变量
l3=0
sum3=0
while line: ##直接用变量名判断是否为空
    print(line)
    l3+=1
    sum3+=len(line)
    line=f.readline() ##循环内还要有，以用于下一轮循环的判断
print('总行数%d,总字符%d'%(l3,sum3))
#3.2 readline()
f.seek(0)
l4=0
sum4=0
while True:
    line=f.readline()
    if line: ##也可以用 len(line)!=0:
        print(line)
        l4+=1
        sum4+=len(line)
    else:
        break
print('总行数%d,总字符%d'%(l4,sum4))
f.close()
