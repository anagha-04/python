
from copy import copy,deepcopy

meghna_fav_fud =[
    ["doas","sambar"],
    ["biriyani","chicken"],
    ["mandhi","beef"]
]

nandhana_fav_fud =copy(meghna_fav_fud)

nandhana_fav_fud[0][0]="chapathi"  #this is shalow copy only outer will change

nandhana_fav_fud=deepcopy(meghna_fav_fud)   #this is deepcopy it will change the outer and nested object

nandhana_fav_fud[1][0]="beef biriyani"

print(meghna_fav_fud)
print(nandhana_fav_fud)