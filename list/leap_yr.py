

yrs = [1900,1901,1902,1903,1904,2000,2024,2021,2011]

print("Leap years are")
for i in yrs:
    
    if i%100==0 and i%400==0 or i%100!=0 and i%4==0:

        print(i)
