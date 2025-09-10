
def decorator(fn):

    def inside_fn(n1,n2):

        if n1<n2:

            (n1,n2)=(n2,n1)

        return fn(n1,n2)

    return inside_fn   





@decorator
def sub(n1,n2):

    return n1-n2

@decorator
def div(n1,n2):

    return n1/n2

print(sub(5,10))
print(div(5,10))