

expense = [10000, 12000 ,13000, 14000]

expense[1] = 12500

print(expense)

#indexing

for i in range(0,len(expense)):


    print(expense[i])

#iteration

# for e in expense:

#     print(e)

total = 0

for e in expense:

    total+=e
print("total expenses: ",total)

# total_exp = 0

# for i in range(0,len(expense)):

#     total_exp+=expense[i]

# print(total_exp)


highest_expense = max(expense)

print(highest_expense)


avg= total/len(expense)

print("averge expense=", avg)



    
                 