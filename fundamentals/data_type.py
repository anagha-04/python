num = 343

print(type(num))

name = "anagha anil"

print(type(name))

number = 23.34

print(type(number))

is_present = True

print(type(is_present))


# read bill_total

#read number of dines

#read tip_amount

#calculate individual split

bill_amount = int(input("enter bill amount:"))

dines = int(input(" number of dines:"))

tip_amount = int(input("enter tip amount"))

total_amount = bill_amount + tip_amount

individual_split  = total_amount / dines

print(individual_split)