
def last_digit_max(num1,num2):

    if num1%10 > num2%10:

        return num1
    else:
        return num2
    
print(last_digit_max(129,106))