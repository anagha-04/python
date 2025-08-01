weight_in_kg = int(input("enter your weight_in_kg:"))

height_in_cm = int(input("enter your height_in_cm:"))

height_in_meter = height_in_cm / 100

bmi = weight_in_kg/height_in_meter**2

print("person weight",weight_in_kg ,"and height", height_in_meter,"BMI=",bmi)