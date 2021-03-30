# Program to input eight number from user and display all unique number
a = int(input("Enter first number:",))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter fourth number:"))
e = int(input("Enter fifth number:"))
f = int(input("Enter sixth number:"))
g = int(input("Enter seventh number:"))
h = int(input("Enter eighth number:"))
numbers = {a, b, c, d, e, f, g, h}
sorted(numbers) # I used this to arrange the number in ascending order
print(numbers)