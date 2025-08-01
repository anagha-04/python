

number = int(input("enter a number:"))

orginal = number

sum = 0

count = len(str(number))

while(number!=0):

    digit = number%10

    exponent = digit**count

    sum = sum+exponent

    number = number//10

if orginal==sum:

    print(orginal,"is amrstrong")

elif orginal!=sum:
    
    print(orginal,"is not a amrstrong")



   