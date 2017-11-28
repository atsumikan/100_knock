st = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

st = st.replace(',','').replace('.','')
li = st.split(' ')
print(li)
numli = []
for obj in li:
    numli.append(len(obj))
print(numli)
