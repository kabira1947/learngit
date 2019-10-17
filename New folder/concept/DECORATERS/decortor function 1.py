def function1():
    print("i am number 1")
def function2(func):
    print("i am number 2 and i will call number 1")
    func()
function2(function1)