for i in range(10):
    print(i)
    if i == 5:
        break # It is used to stop the loop if a condition is given without even completing the range
    else:
        print("This is inside else of for")
    
    ## If a loop is stopped naturally then it goes to else but if it is stopped by giving a condition then the loop stops as break is used
    