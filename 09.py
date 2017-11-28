import random
wordli = input().split(' ')
after = []

for w in wordli:
    if len(w)<=4:
        after.append(w)
    else:
        tmpl = list(w[1:-1])
        random.shuffle(tmpl)
        after.append(w[0] + "".join(tmpl) + w[-1])
print(" ".join(after))
