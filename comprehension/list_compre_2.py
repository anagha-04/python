

words = ["apple","banana","carrot","egg","orange"]

new_words =[w for w in words if w[0].lower() in "aeiou"]
print(new_words)


word_dict =[{w:len(w)}for w in words]
print(word_dict)