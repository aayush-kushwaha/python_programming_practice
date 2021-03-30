# Program to convert celcius to F
# (0°C × 9/5) + 32 = 32°F
def farh(cel):
    a = (cel * (9/5)) + 32 
    return a
print(f"The temperature in Fahrenheit is: {farh(15)}") 

