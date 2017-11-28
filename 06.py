def function(st):
    word = st.split(' ')
    char = list(st)

    word_bigram = []
    char_bigram = []

    for i in range(len(word)-1):
        tmp_list = [word[i],word[i+1]]
        word_bigram.append(tmp_list)
    for i in range(len(char)-1):
        char_bigram.append(char[i] + char[i+1])
    return [word_bigram,char_bigram]

str1 = "paraparaparadise"
str2 = "paragraph"

gram1 = function(str1)[1]
gram2 = function(str2)[1]

X = set(gram1)
Y = set(gram2)

print(X | Y)
print(X & Y)
print(X - Y)

print('se' in X)
print('se' in Y)
