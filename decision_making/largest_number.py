

# read 2 numbers and display largest number
# ------------------------------------------


# num1 = int(input("enter number1:"))

# num2 = int(input("enter number2:"))

# if num1>num2:

#     print("largest number is",num1)

# elif num2>num1:

#     print("largest number is",num2)



# read 3 num and disply largest num
# ----------------------------------


num1 = int(input("enter num1:")) #num9
num2 = int(input("enter num2:")) #num3
num3 = int(input("enter num3:")) #num2


# 9>3 and 9>2

if num1>num2 and num1>num3:
    print ("largest number is",num1)

    # 3>9 and 3>2
elif num2>num1 and num2>num3:
    print("largest number is",num2)


    # 2>9 and 2>3
elif num3>num1 and num3>num2:
    print("largest number is",num3)

