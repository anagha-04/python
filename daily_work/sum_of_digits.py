

number = 999



sum = 0 #9+9+9=27



while(number!=0): #999!=0
    digit = number%10  #999%10=9

    sum = sum+digit  # 0+9=9

    number = number//10 #999//10= 99

orginal=sum #27

new_sum =0
while(orginal!=0): #27!=0

    last_digit = orginal%10 #27%10=7

    new_sum = new_sum+last_digit  # 0+7=7

    orginal = orginal//10  #27//10=2

print(new_sum)

   
