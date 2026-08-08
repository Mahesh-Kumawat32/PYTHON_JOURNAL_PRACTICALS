l = [1,2,3,7]

#INSERTION ON LIST
print("After insertion")
l.append(12)
l.insert(0,20)
print(l)

#SEARCHING ON LIST
print("\nSearching Operations")
print(l.index(12))

#SORTING A LIST
print("\nAfter Sorting")
l.sort()
print(l)

#DELETION ON LIST
print("\nAfter Deletion")
l.remove(12)
l.pop()
print(l)

