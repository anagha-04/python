

# set number
# set count
# loop
# last digit
# increment count
# floor(remove last digit)
# print count


number =65456784567

count = 0

while(number!=0):

    digit = number%10

    count += 1

    number = number//10
print(f"number of digits {count}")