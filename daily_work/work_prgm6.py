

year = 1879

while(year<=2025):
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        print(year)

    year+=1