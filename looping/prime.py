

num = int(input("enter a number:"))

is_prime = True

for i in range(2,num):

    if num%i==0:

        is_prime = False

    break

result = "prime number" if is_prime==True else "not prime"

print(result)

