
def sum_of_n(num):

    if num==0:

        return 0
    return num+sum_of_n (num-1)

print(sum_of_n(6))


def sum_of_digits(num):

    if num == 0:

        return 0
    
    return num%10+sum_of_digits(num//10)

print(sum_of_digits(1235))
