# Program to find the sum of first n natural number using while loop
# n = int(input("Enter the number: "))
# i = 1
# while (i<=n):
#     i = i+1
#     print(a+a)
num = int(input("Enter a number: "))  
  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   # use while loop to iterate un till zero  
   while(num > 0):  
       sum = sum + num  
       num = num - 1  
   print("The sum is",sum)  