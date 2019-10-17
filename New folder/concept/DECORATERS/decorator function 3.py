def funtion1(func):
    def inner(x,y):
        if y==0:
            return "enter a value greater than 0"
        return func(x,y)
    return inner
@funtion1
def divfunc(a,b):
    return a/b
print(divfunc(4,0))
print(divfunc(4,8))

