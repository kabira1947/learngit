class a():
    def father(self):
        return "i am father"
class b(a):
    def mother(self):
         return "I am mother"
class c(a):
    def son(self):
        return "i am son"

C=c()
B=b()
print(B.father())
print(C.father())

