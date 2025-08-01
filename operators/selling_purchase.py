

purchase_price =int(input("enter purchase_price"))

profit_margin = int(input("enter profit in %"))

profit = (profit_margin/100)*purchase_price

gst = 8

selling_price = purchase_price + profit

gst_amount = (gst/100)*selling_price
 
total_cost = selling_price + gst_amount

print(total_cost)