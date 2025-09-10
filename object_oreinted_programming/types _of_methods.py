
# 1)instance
# 2)class
# 3)static


class Employee:

    def __init__(self,id,name):

        self.id = id

        self.name = name

    def display_employee(self):    #instance method

        print(self.id,self.name)

    @classmethod

    def class_method_demo(cls):    #class method

        print("inside class method")

    @staticmethod

    def static_method_demo():    #statc method

        print("inside ststic method")


Employee.class_method_demo()

Employee.static_method_demo()
