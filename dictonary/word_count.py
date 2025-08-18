

text = "hello haii haii hello hello haii hello"

words = text.split( )

wc={}

for w in words:

    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1

print(wc)

       

