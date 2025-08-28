
file_path ="C:\\Users\\anagh\\OneDrive\\Desktop\\development _journey\\python_works\\file_operations\\employee.csv"

fr = open(file_path,"r")

all_employees = []

for line in fr:

   # line = line.rstrip("\n")

    #data = line.split(",")

    data = line.rstrip("\n").split(",")

    dictionary = {"id":data[0],"name":data[1],"departement":data[2],
                  "salary":data[3],"email":data[4],"location":data[5]}

    all_employees.append(dictionary)

print(all_employees)

names = [e.get("name") for e in all_employees]

print("employee names: ",names)

ekm_employee =[e.get("name") for e in all_employees if e.get("location") == "ekm"]

print("ekm employees name :",ekm_employee)

max_salary = max(all_employees,key=lambda e:e.get("salary"))

print("highest salary employee : ",max_salary)


min_salary = min(all_employees,key=lambda e:e.get("salary")).get("salary")

min_salary_employee = [e.get("name") for e in all_employees if e.get("salary")== min_salary]

print("lowest salary employee: ",min_salary_employee)