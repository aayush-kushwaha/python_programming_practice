# Creating an empty set
b = set()
print(b)
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)  # Adding value repeatedly does not changes a set
b.add(5)  # Adding value repeatedly does not changes a set
b.add((4, 5, 6))   # Tuples can be added as it is not mutable

## Accessing Elements
# b.add([4, 5, 6]) #Cannot add list or dictionary to sets and these are mutable 
# b.add({4: 5})    #Cannot add list or dictionary to sets and these are mutable 
print(b)

## Length of the Set
print(len(b)) # Prints the length of the set

## Removal of an Item    
b.remove(5) # Removes 5 from the set b
# b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(b)

print(b.pop()) # Randomly pops or removes the number from the set
print(b)