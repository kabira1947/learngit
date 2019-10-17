a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.difference(b))
print(a.union(b))
print(a.intersection(b))
print(a.symmetric_difference(b))
print(len(a))
print(a.update(b))

a1={"Jake", "John", "Eric","John", "Jill"}

a1.remove("Jake")
print(a1)

a1.add("Jake")
print(a1)

a.discard("Jill")
print (a1)

a1.pop()

print(a1)

a2 = {"Jake", "John", "Eric"}

a2.clear()

print(a2)

a3 = {"Jake", "John", "Eric"}
print(a3)
del a3

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
#print(fruits | more_fruits)
fruits.update(more_fruits)
print(fruits)

'''add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others '''
