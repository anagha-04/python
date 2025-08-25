

lst = [1,2,4,6,7,9]
#      0,1,2,3
#      i j

for i in range(0,len(lst)-1):

    j= i+1

    difference = lst[j] - lst[i]

    if difference!=1:

     print(lst[i]+1)
    
        