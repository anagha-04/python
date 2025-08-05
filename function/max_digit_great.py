

def max_odd_number(number):

    while number!=0:

        digit = number%10

        if digit%2!=0:

            print(number)
            break
        number = number//10
max_odd_number(4372)
            
