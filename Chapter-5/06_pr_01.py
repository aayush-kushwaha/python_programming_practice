'''
Program to create dictioanry of Hindi words with values as their English translation. And provide option to look it up.
'''

myDict = {
    "Fan": "Pankha",
    "Dabba": "Box",
    "Vastu": "Item"
}
print(myDict.keys())
a = input("Enter Hindi word:\n",)
# print("The English word is:", myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The English word is:", myDict.get(a)) # If an item is not in the dictionary then its better to use .get 
