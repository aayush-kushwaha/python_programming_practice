myDict = {
    "Fast": "In a quick manner",
    "Harry": "A coder",
    "Marks": [1,2,5],
    "anotherDict": {'harry': 'Player'},
    1: 2
}

#Dictionary Methods
print(myDict.keys()) # Prints the keys of the dictionary
print(list(myDict.keys())) # Converts it in the list
print(myDict.values()) # Prints the values of the dictionary
print(myDict.items()) # prints the (key, value) for all content of the dictionary
print(myDict) 
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Subham": "Friend",
    "Harry": "A Dancer" # Here "Harry": "A coder" is changed into "Harry": "A Dancer"
}
myDict.update(updateDict)
print(myDict)

print(myDict.get("Harry")) # Prints value associated with key "harry"
print(myDict["Harry"]) # Prints value associated with key "harry"

# The difference between .get and [] syntax in dictionaries?
print(myDict.get("Harry2")) # Returns None as Harry2 is not present in the dictionary
print(myDict["Harry2"]) # throws an error as Harry2 is not present in the dictionary