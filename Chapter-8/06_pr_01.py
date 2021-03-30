def greatest_num(num1, num2, num3):
    if (num1 > num2):
        if (num1 > num3):
            return num1
        else:
            return num3
    if (num2>num3):
        return num2
    else:
        return num3
m = greatest_num(3, 5, 234)
print(f"The greatest number is: {m}")
            
