# Program to find whether a given username contains less than 10 characters or not

username = input("Enter username: ")

if (len(username) > 10):
    print("Username contains more than 10 characters")
else:
    print("Username doesn't contain more than 10 characters")
