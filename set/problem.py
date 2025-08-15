

st1 = {10,20,30,40}

st2 = {100,10,200,20,300}

#common elements

intersection_set = st1.intersection(st2)

print(intersection_set)


#union

union_set = st1.union(st2)

print(union_set)



#difference


unique_set = st1.difference(st2)

print(unique_set)


#adding new object to the set


menu = {"lime","orange_juice", "mango_juice"}

menu.add ("apple_juice")

print(menu)


#subset


st_a = {10,20,30,100}

st_b = {100,10,20,200,30}


print(st_a.issubset(st_b))