

#comprehension
#Easy way to creating list,dict,set from an iteration

#syntax
#[expression  iteration  condition]


arr = [2,5,4,8,9,12,13,10,7]

square_list = [num**2 for num in arr]
print("square list", square_list)


cube_list = [num**3 for num in arr]
print("cube list", cube_list)


even_num = [num for num in arr if num%2==0]
print("even number ",even_num)


odd_num = [num for num in arr if num%2!=0]
print("odd numbers ",odd_num)


num_gt_five = [num for num in arr if num>5]
print("greater than 5 ",num_gt_five)
