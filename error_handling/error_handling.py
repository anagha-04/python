# num1 = int(input("enter a number1: "))

# num2 = int(input("enter a number2: "))

# try: 
#      div_res =num1/num2

#      print(div_res)

# except:
     
#      print("error occured")

# print("send a text msg to the user phnone number")

# print("send a email verfication ")





num1 = int(input("enter a num1:" ))

num2 = int(input("enter a num2:" ))


try:
    div_res = num1/num2

    print(div_res)

except Exception as e:

     num2 = int(input("enter num2: "))

     div_res = num1/num2

     print(div_res)

finally:
     print("send a text msg to the user phnone number")

     print("send a email verification")