bill_amount = int(input("enter bill amount"))

dines = int(input("enter number of dines"))

tip_amount = (12/100)*bill_amount

gst =( 8/100)*bill_amount

total_amount = bill_amount + tip_amount + gst

individual_split = total_amount/dines

print(individual_split)