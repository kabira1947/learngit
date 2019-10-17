def function1(func):
    def inner(*args):
        list1=[]
        list1=args[1:]

        for i in list1:
            if i==0:
                return "enter a number greater than 0"
        return func(*args)
    return inner
@function1
def div1(a,b):
    return a/b
@function1
def div2(a,b,c):
    return a/b/c
print(div1(10,0))
print(div2(0,4,10))
