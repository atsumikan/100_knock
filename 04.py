st = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

st = st.split(' ')
dic = {}

for i in range(len(st)):
    if i==1 or i==5 or i==6 or i==7 or i==8 or i==9 or i==15 or i==16 or i==19:
        dic.append(st[i][0] + st[i][1])
    else:
        dic.append(st[i][0])
print(dic)
