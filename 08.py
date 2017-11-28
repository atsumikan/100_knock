def cipher(st):
    after = ""
    for c in st:
        if ord(c) < ord('a') and ord(c) > ord('z'):
            after += c
        else:
            after += chr(219-ord(c))
    return after

st = "paraparaparadise"
print(st)
st = cipher(st)
print(st)
st = cipher(st)
print(st)
