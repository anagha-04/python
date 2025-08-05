num = int(input("enter a number: "))

count = 0

for i in range(100):

   if num == 0 and count !=0:
      break
   elif num ==0 and count==0:
      count=1
      break
   num = num//10
   count += 1
print(count)