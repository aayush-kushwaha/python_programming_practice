#Concatenating two strings
# greeting = "Good Morning "
# name = "Aayush"
# c = greeting + name
# print(c) 


#Indexing
# name = "Aayush"
# print(name[4])
# name[3] = d #Doesn't work

#Slicing
# name = "Harry"
# print(name[1:4]) #-->Prints from a to y #[1:4] means from 1 to 3
# print(name[:4]) #--> is same as [0:4]
# print(name[1:]) #--> is same as [1:5]
# c = name[-4:-1] #--> is same as [1:4]

name = "HarryIsGood"
d = name[0::2]# It means [0:11:2] which means it has skip value of 2 
              # which will print H and it will skip a then print r then
              # skip r then print y then skip I and so on.............!!
print(d)
