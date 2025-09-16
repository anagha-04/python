def abs_dec(func):

    def wrapper(num1,num2):

        return func(abs(num1),abs(num2))
    
    return wrapper

@abs_dec
def add_numbers(num1,num2):

    return num1+num2

print(add_numbers(-5,10))