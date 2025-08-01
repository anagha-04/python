

year = int(input("enter a year:"))

if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
    print(year,"is a leep year")

else:
    print(year,"not a leep year")