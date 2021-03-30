# # Program to find whether a given number is prime or not
# a = int(input("Enter the number: "))
# prime = True
# for i in range(2, a):
#     if (a%2 == 0):
#         prime = False
#         break
# if prime:
#     print("The number is prime")
# else:
#     print("The number is not prime")

a = int(input("Enter a number: "))
for i in range(2, a):
    if a%i == 0:
        print("The number is not prime! ")
        break
else:
    print("The number is prime! ")