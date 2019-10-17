#Closure

def outer():
    x=3
    def inner():
        y=3
        result= x+y
        return  result
    return inner()
a=outer
print(a())
