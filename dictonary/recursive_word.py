

text = "this is a python program to find most recursive word this python program is simple"

words = text.split()

word_count = {}

for w in words:

    if w in word_count:

        word_count[w]+=1

    else:

        word_count[w]=1

srt_wc = sorted(word_count,reverse=True,key=word_count.get)

print(srt_wc)