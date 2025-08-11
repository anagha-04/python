

text = input("enter a text: ").casefold()

vowels ="aeiou"

v_count = 0

c_count = 0

for ch in text:

    if vowels in text:

        v_count= v_count+1

    else:
    
        c_count+=1
print("vowels",v_count)

print("consoant",c_count)
    



