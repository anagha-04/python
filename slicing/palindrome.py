

arr =["word","madam","car","amma"]


print("palindrome words: ")
for w in arr:

 if w==w[::-1]:

        print(w)
        


        
palindrome = [w for w in arr if w ==w [::-1]]
print("palidrome words:",palindrome)