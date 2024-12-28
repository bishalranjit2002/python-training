#this_is_comment
print("this_is_my_first_code")

#data type in python
print(2+2)#this is integer datatype
print(2.5+2.5)#this is float datatype
print("hello world")#this is string datatype
print(10>11)#this is boolean datatype
print(["bishal","ram","hari"]) #this is list data type


#variable
username ="bishal"
print(username) #this is variable in python

#find type of variable
print(type(username)) #this is type of variable in python

#reassign variable
username = "ram"
print(username) #this is reassign variable in python

#conditional statement
#if else
if username == "ram":
    print("username is ram") #this is if else statement in python
else:
    print("username invalid")

#using elif
status = 200
if status == 200:
    print("status is 200")
elif status == 400:
    print("status is 400")
else:
    print("status is invalid")


#for loop
for i in range(10):
    print("hello")

#while loop
i = 0
max_device = 10

while i<max_device:
    print("you can connect")
    i=i+1
print("you cannot connect")