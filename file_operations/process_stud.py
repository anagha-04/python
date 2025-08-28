

all_students_path = "C:\\Users\\anagh\\OneDrive\\Desktop\\development _journey\\python_works\\file_operations\\all_students.txt"
failed_students_path = "C:\\Users\\anagh\\OneDrive\\Desktop\\development _journey\\python_works\\file_operations\\failed_students.txt"
passed_students_path = "C:\\Users\\anagh\\OneDrive\\Desktop\\development _journey\\python_works\\file_operations\\passsed_students.txt"

f_all_students = open(all_students_path,"r")

f_failed_students = open(failed_students_path,"r")

f_passed_students = open(passed_students_path,"w")


all_students_set = set()

failed_students_set = set()

for name in f_all_students:

    all_students_set.add(name.rstrip("\n"))

print(all_students_set)

for name in f_failed_students:

    failed_students_set.add(name.rstrip("\n"))

print(failed_students_set)


f_passed_students = all_students_set.difference (failed_students_set)

print(f_passed_students)

for name in f_passed_students:

    passed_students_path.write(name+"\n")

print(passed_students_path)