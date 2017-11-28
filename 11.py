#cording:utf-8
counter = 0
f = open('hightemp.txt','r')
content = f.readlines()
f.close()
for i in range(len(content)):
    content[i] = content[i].replace('\t',' ')
print(content)
