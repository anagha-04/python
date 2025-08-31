

class Employee:

    id = int

    name = str

    department = str

    salary = int

    def set_employee(self,id,name,department,salary):

        self.id = id

        self.name = name

        self.department = department

        self.salary= salary

    def display_employee(self):

        print(self.id,self.name,self.department,self.salary)

emp_instance1 = Employee()

emp_instance2 = Employee()

emp_instance2.set_employee(1001,"ravi","HR",60000)

emp_instance2.display_employee()