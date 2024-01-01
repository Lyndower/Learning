#将file1.txt文件中存放着的每行按逆序输出到file2.txt文件中

f1=open('file1.txt','r').readlines()
print(f1)
f2=open('file2.txt','w+')#'w+'打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
for i in range(len(f1),0,-1):
    f2.write(f1[i-1])
f2.seek(0)
print(f2.read())
f2.close()
