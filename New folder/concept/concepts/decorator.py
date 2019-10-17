def dec(func1):
    def nowex():
        print("Executing Now")
        func1()
        print("executed")
    return nowex()

@dec
def whoi():
    print("I am working")

whoi()