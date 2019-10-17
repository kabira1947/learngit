class a():
    def father(self):
        return "i am father"
class b(a):
    def mother(self):
         return "I am mother"
class c(b):
    def son(self):
        return "i am son"

C=c()
B=b()
print(C.mother())
print(C.son())
print(B.father())
