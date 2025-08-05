

num = int(input("enter a three digit number :"))

orginal = num

sum=0

for i in range(3):

    digit = num%10

    sum = sum+digit**3

    num= num//10
if sum == orginal:
    print("armstrong number")
else:
    print("not an armstrong")

