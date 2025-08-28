

f_path ="C:\\Users\\anagh\\OneDrive\\Desktop\\development _journey\\python_works\\file_operations\\food_logs.csv"

fr = open(f_path,"r")

food_logs =[]

for line in fr:

    data = line.rstrip("\n").split(",")


    if len(data)>1:
        

        dictonary = {"date":data[0],"meal_type": data[1],"name": data[2],"serving_size":data[3],"calories":data[4]}

        food_logs.append(dictonary)

print(food_logs)

