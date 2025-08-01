

# set number
# set sum
# loop
# extract last digit 
# add last digit with sum
# floor
# print


number = 234

sum = 0

while(number!=0):  #234!=0

    digit = number%10 #234%10=4

    sum += digit #sum = sum+digit=0+4=4

    number = number//10 #234//4=23
print("sum is",sum)

