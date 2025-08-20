

text = "goodmorning"

chr_count = {}

for ch in text:

    if ch in chr_count:

        chr_count[ch]+=1

    else:

        chr_count[ch]=1

print(chr_count)


#another method

text = "goodmorning"

chr_count = {}

for ch in set(text):

    chr_count[ch]=text.count(ch)

print(chr_count)