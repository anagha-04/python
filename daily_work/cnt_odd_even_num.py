

num = 123456789

count_odd = 0

count_even = 0

while(num != 0):
    
    digit = num%10  #digit=7

    num = num//10  # num=1346 

    if digit%2==0: #7==0

        count_even= count_even+1

    elif digit%2!=0:

         count_odd = count_odd+1

print( "even",count_even)

print("odd",count_odd)




    
    

   
    
