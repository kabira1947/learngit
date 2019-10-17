
def add_to(num, target=[]):
    target.append(num)
    return target
print(add_to(3))
print(add_to(5))



def add_too(num, target=[]):
    target.append(num)
    return target

add_too(1)
# Output: [1]

add_too(2)
# Output: [1, 2]

add_too(3)
# Output: [1, 2, 3]