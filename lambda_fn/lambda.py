
#short one line function without name (anonymous = without name)

#syntax
#lambda p1,p2...pn:expression


sub = lambda n1,n2:n1-n2

print(sub(30,10))



cube=lambda n1:n1**3

print(cube(3))


#last_digit_max(121,128)

last_digit_max=lambda n1,n2: n1 if n1%10> n2%10 else n2

print(last_digit_max(121,128))