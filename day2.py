#function in python

#define a function
def greet():
    print("Hello, World!")


#calling a function
greet()

# using function with if else
def display_investigation_message():
    print("investigate activity")

application_status = "potential concern"
email_status = "okay"

if application_status == "potential concern":
    print("application_log:")
    display_investigation_message()

if email_status == "potential concern":
    print("email log:")
    display_investigation_message()


#parameter in function

def greeting(name):
    print("hello",name)

greeting("bishal")


#using more than one parameter

def greeting2(fname,lname):
    print("hello",fname,lname)
greeting2("bishal","ranjit")



#return statement in function

def add(num1,num2):
    sum = num1+num2
    return sum
print(add(2,3))

#builtin function 

#range function

for i in range(0,10):
    print(i)

#max and min function
a=1
b=2
c=3

print("maximum value is",max(a,b,c))
print("minimum value is",min(a,b,c))


#sorted function
username=["suman","ram","hari"]
print(sorted(username))

#modules from the Python Standard Library
import statistics
monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]
mean_failed_attempts = statistics.mean(monthly_failed_attempts)
print("mean:", mean_failed_attempts)

