# Factorial(n!) means # n! = 1 X 2 X 3 X 4 X 5 X 6 X ...............X n
# 5! = 1 X 2 X 3 X 4 X 5
a = int(input("Enter a number to calculate factorial! "))
factorial = 1
for i in range(1, a+1):
    factorial = factorial * i
print(f"The factorial of {a} is: {factorial} ")