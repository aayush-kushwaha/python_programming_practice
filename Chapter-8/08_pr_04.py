# Recursive Program to calculate the sum of first n natural numbers
# def mySum(n):
#     sum = (n-1) + n
#     return sum

def mySum_recursive(n):
    if n<=1:
        return n
    else:
        return mySum_recursive(n-1)+n

print(f"The sum is: {mySum_recursive(5)}") 
