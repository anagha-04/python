

phn = {"code":"sh120",
       "company":"redmi",
       "color":"black",
       "price":20000,
       "offer":1000}

phn["price"]=22000

print(phn)

phn["is_available"]=True

print(phn)

print(phn["company"])

if "offer" in phn:

    phn["offer"]+=400 #update

else:

    phn["offer"]=1000 #adding

print(phn)