#polymorphsym

#more than one form(many forms)

#method overloading

#(within same class same method name but different number of parameters)



class Calculate:

    def add_numbers(self,num1,num2):

        print(num1+num2)

    def add_numbers(self,num1,num2,num3):

        print(num1+num2+num3)

    def add_numbers(self,num1,num2,num3,num4):

        print(num1+num2+num3+num4)

cal_instance = Calculate()

cal_instance.add_numbers(10,20,30,40)


class Operation:

    def add(self,*args):

        print(sum(args))
operation_instance = Operation()

operation_instance.add(10,20,30)
operation_instance.add(10,20,10,30)

# (*args) and (*kwargs)

#it take any number of parameters as a tuple

def add_numbers(self,*args):
    
    print(sum(args))

    add_numbers(10,10,30,40)
    add_numbers(2,3,4)
    add_numbers(1,2)

