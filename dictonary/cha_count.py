

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

char_count ={}

for ch in set(text):

    char_count[ch] = text.count(ch)

print(char_count)

max_frequency = 0

max_frequency_dictionary = {}

for k,v in char_count.items():

    if v>max_frequency:

        max_frequency = v

        max_frequency_dictionary.clear()

        max_frequency_dictionary[k]=v
        
print(max_frequency_dictionary)