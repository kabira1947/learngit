class a():
    def father(self):
        return "i am father"
class b(a):
    def mother(self):
         return "I am mother"
class c(a):
    def son(self):
        return "i am son"
class d(c,b):
    def daughter(self):
        return "i am daughter"
C=c()
D=d()
B=b()
print(D.mother())
print(D.son())
print(C.father())
print(B.father())
