# Program to print pass if the marks of indvivdula subject 33 and total subject pereventage is 40
sub1 = int(input("Enter subject 1: "))
sub2 = int(input("Enter subject 2: "))
sub3 = int(input("Enter subject 3: "))
percentage = ((sub1 + sub2 + sub3) / 3)

# DOubt_needed to  resolved:
# Above coding in the comments is wrong or maybe wrong!! Just wanted to ask why???
# if (percentage >= 40 and sub1 > 33):
#     print("pass")
# elif (percentage >= 40 and sub2 > 33):
#     print("pass")
# elif (percentage >= 40 and sub3 > 33):
#     print("pass")
# else:
#     print("fail")



if (sub1<33 or sub2<33 or sub3<33):
    print("You have failed because you have less than 33% in one of the subject!")
elif((sub1 + sub2 + sub3)/3 < 40):
    print("You have failed becasue you have less than 40% in total percentage!")
else:
    print("Congratulations!!!! You have passed the exam....")
