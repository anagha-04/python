

#text = "A B C A A C D"

#char = text.split( )

#wc ={}                 # empty dic

#for w in char:         #A in char

    #if w in wc:         #A in wc

        #wc[w]+=1        #alredy A exist then update

    #else:

        #wc[w]=1          #there is no A so add

#print(wc)


text = "A B C A A C D"

char = text.split()

wc = {}

for w in char:

    if w in wc:

        print("first recursive word is",w)

        break
    else:
        wc[w]=1

