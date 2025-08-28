


path = "C:\\Users\\anagh\\OneDrive\\Desktop\\development _journey\\python_works\\file_operations\\palindromeee.txt"

fw =open(path,"w")

word =["haii","hello","madam","racecar","pangram"]

for w in word:

     if w==w[::-1]:
          
          fw.write(w+"\n")
