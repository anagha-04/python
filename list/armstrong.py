

number = [151,152,153,1634,8891,345,678]

for num in number:

    exponteial = len(str(num))
    
    sum = 0
    
    for digit in str(num):

        sum+= int(digit)**exponteial

        if sum==num:
            print(num)