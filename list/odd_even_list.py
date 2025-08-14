

arr =[1,10,11,12,34,35]

arr_even = []

arr_odd = []

for num in arr:

    if num%2==0:
        arr_even.append(num)

    else:
        arr_odd.append(num)
        
print(arr_even)

print(arr_odd)


