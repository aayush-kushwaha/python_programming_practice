# Program to print the sum of n number of natural number
n = int(input("Enter a number: "))
i = 1
sum = 0
while (i<=n):
    sum = sum + i
    i = i + 1
print(f"The sum of natural number is: {sum}")