

text = "this is a python program to find most recursive word this python program is simple"

words = text.split()

word_count = {}

for w in set(words):

    word_count[w]= words.count(w)

print(word_count)