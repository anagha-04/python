attendance = ["H","P","P","P","P","L","H","H","P","P","P","P","L","H"]

working_day = 0

for a in attendance:
    
    if a != "H":

        working_day+=1
print("working Days =",working_day)


leave = 0

for a in attendance:

    if a=="L":

        leave+=1
print("total leave =",leave)