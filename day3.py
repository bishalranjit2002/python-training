#string
string="hello"#declaring string

#convert other datatype into string using str()
num =123
print(str(num))#converting int into string

#find the length of string using len()
string="bishal"
print(len(string))#length of string

#string concatation (joing two string)
print("hello" +"world")

#method in string
#1. lower()
print("HELLO".lower())

#2. upper()
print("hello".upper())

#slicing in python
print("bishal"[1:4])

#searching in string
#use index method
print("hello".index("e"))

#learning about list
list = ["a","b","c"]
print(list)

#accessinng in list
print(list[0])

#list concatatioon
list1=["a","b","c"]
list2=[1,2,3]
print(list1+list2)

#string are inmutable where as lsit are mutable
list1[1]="d"
print(list1)

#method in list
#insert()
list1 = ["a", "b", "c"]
list1.insert(1, "g")  # Inserts "g" at index 1
print(list1)  # This will print the modified list

#remove()
list1.remove("g")
print(list1)
