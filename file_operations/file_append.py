

path ="C:\\Users\\anagh\\OneDrive\\Desktop\\development _journey\\python_works\\file_operations\\greetings.txt"

fa = open(path,"a")

food_items =["idli","dosa","putt"]

for food in food_items:

    fa.write(food+"\n")