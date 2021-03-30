def greet(name="Stranger"): # If we specify name="Stranger" in the line containing def,--
    return("Hello! " + name) # --(cont'd) this value is used when no arguement is passed 
greet1 = greet()
print(greet1) 
greet2 = greet("Aayush")
print(greet2)