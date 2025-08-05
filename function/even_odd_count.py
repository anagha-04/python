

def odd_even_count(num): #1234

    even_count = 0

    odd_count = 0

    while(num!=0): #1234!=0

        digit = num%10 #1234%10=4

        if digit%2==0: #4%2==0

            even_count= even_count+1 #ec=1

        else:
            odd_count= odd_count+1 #oc=1

        num= num//10

    print(even_count)
    print(odd_count)

odd_even_count(1234)


