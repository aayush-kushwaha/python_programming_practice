# Program which finds out whether a given name is present in a list or not

name_list = ["aayush", "roshan", "harry" , "anjali", "shivam"]
name = input("Enter your name: ")

if (name in name_list):
    name = True
else:
    name = False

if(name):
    print("Its present in List")
else:
    print("Its not present in List")



# This code is also right
# if (name in name_list):
#     print("Its present in List")
# else:
#     print("Its not present in List")
