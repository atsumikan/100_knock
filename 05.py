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
    
st = "I am an NLPer"
res = function(st)
print(res[0])
print(res[1])
