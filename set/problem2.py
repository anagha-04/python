

sachin_frnds ={"rahul","abhi","aswin","akshay","sreejith"}

dhoni_frnds ={"sayooj","vishnu","aswin","nirmal","akshay"}

#display all frnds

frnds= set(sachin_frnds).union(dhoni_frnds)

print(frnds)

#unique frnds


unique_frnds=set(sachin_frnds).difference(dhoni_frnds)

print(unique_frnds)


#mutal frnds

same_frnds = set(sachin_frnds).intersection(dhoni_frnds)

print(len(same_frnds))