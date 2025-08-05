
num = int(input("enter a number : "))

reverse = 0 

for i in range(num):

    digit = num%10

    reverse = reverse *10+digit

    num = num//10

    if num == 0 and reverse!=0:
        break

print(reverse)