'''def function1(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner
def function2():
    return "good morning I am 2"
print(function2())

a= function1(function2)
print(a())
'''
#or

def function1(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner
@function1
def function2():
    return "good moring I am 2"
print(function2())

#a= function1(function2)
#print(a())
