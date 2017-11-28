#cording:utf-8
counter = 0
f = open('hightemp.txt','r')
content = f.readlines()
for obj in content:
    counter += 1
f.close()
print("linecount:{}".format(counter))
print(str(counter))
