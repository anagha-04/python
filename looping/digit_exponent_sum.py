

# set number
# count
# sum=0


# loop
    # last_digit
    # exponent=last digit**count
    # sum= sum +exponent
    # remove last digit
# printsum

number = 153

count = len(str(number))

sum = 0

while(number!=0):

    last_digit = number%10

    exponent = last_digit ** count

    sum = sum + exponent

    number = number//10

print(sum)


