class a():
    def father(self):
        return "i am father"
class b():
    def mother(self):
         return "I am mother"
class c(b,a):
    def son(self):
        return "i am son"

C=c()
print(C.mother())
print(C.son())
print(C.father())