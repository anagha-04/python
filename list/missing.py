

lst = [1,2,4,5]
#      0,1,2,3
#      i j

for i in range(0,len(lst)-1):

    j= i+1

    difference = lst[j] - lst[i]

    if difference!=1:

        print(lst[i]+1,"is missing Number")

        break