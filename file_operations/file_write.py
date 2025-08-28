
fw = "C:\\Users\\anagh\\OneDrive\\Desktop\\development _journey\\python_works\\file_operations\\greetings.txt"

fw = open(fw,"w")

greetings_list =["good morning","good evening","good night"]

for g in greetings_list:

    fw.write(g+"\n")