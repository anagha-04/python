
def abs_num(fun):

    def wrapper(num1,num2):

        return fun(abs(num1),abs(num2))
    
    return wrapper





@abs_num
def add_numbers(num1,num2):

    return num1+num2

print(add_numbers(-10,5))



class Employee:

    def __init__(self,id,name,department):

        self.id = id

        self.name = name

        self.department = department


    @property
    def get_name(self):

        print(self.name)

    employee_instance1 = Employee(123,"hari","hr")

    employee_instance1.get_name

    print(employee_instance1.name)

    print(employee_instance1.id)


        