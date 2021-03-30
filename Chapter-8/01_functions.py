def percentage(marks):               
    p = (sum(marks))/400 * 100
    return p                    #It is reusable code which takes others variable input and calculate it and it saves time and it helps to make code smaller(laut chalo value k saath) 

marks1 = [77, 88, 99, 69]
percentage1 = percentage(marks1)

marks2 = [66, 77, 88, 85]
percentage2 = percentage(marks2)

print(percentage1, percentage2)
