def function1(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner
def function2(func):
    def onner():
        str2=func()
        return str2.split()
    return onner
@function2
@function1
def function_dec():
    return "hello I am likun"
print(function_dec())