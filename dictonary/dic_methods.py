

# def get(key)
# def pop(key)
# def keys()
#def update()

fruits = {"a":"apple","b":"banana","c":"cherry","d":"dragon_fruit"}

print(fruits.get("a"))

#def pop(key)

poped_value=fruits.pop("c")

print(poped_value)

print(fruits)


#def keys()

print(fruits.keys())

for k in fruits:
    print(k)


#def update()

fruits.update(o="orange")

fruits.update(e="egg-fruit")

print(fruits)

