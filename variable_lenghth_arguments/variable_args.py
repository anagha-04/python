
def display_Person_details(*args):

    print(args)

    name=args[0]

    print(name)

    address = args[1]

    print(address)

display_Person_details("tom","street1","london","uk")



#**kwargs

def student_details(**kwsrgs):#("roll":12,"name":"jerry","address":"street1","place":"london")

    print(kwsrgs)
    


student_details(roll=12,name="jerry",address="streeet2",palce="london")