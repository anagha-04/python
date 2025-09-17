class Calculator:

    def operation(self,*args,**kwargs):

        if kwargs.get("op")=="+":
            return args[0]+args[1]
        
        if kwargs.get("op")=="-":

            return args[0]-args[1]

calculator_instance1 =Calculator()

print(calculator_instance1.operation(10,20,op="+"))
print(calculator_instance1.operation(60,20,op="-"))