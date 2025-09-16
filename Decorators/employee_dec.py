class Employee:

    def __init__(self,id,name,department):

        self.id = id

        self.name = name

        self.department = department


    @property
    def get_name(self):

        return(self.name)

employee_instance = Employee(123,"hari","hr")

employee_instance.get_name 

print(employee_instance.name)

print(employee_instance.id)


        