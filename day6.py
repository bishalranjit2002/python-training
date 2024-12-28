#learning automation in python

#reading a file in python

with open("file.txt", "r") as file:
    data = file.read()
    print(data)


#parsing in python
#pasring is used to convert string into list. here we use split()

with open("file.txt", "r") as file:
    data = file.read()
    list = data.split()
print(list)

approved_users = "elarson,bmoreno,tshah,sgilmore,eraab"
print("before .split():", approved_users)
approved_users = approved_users.split(",")
print("after .split():", approved_users)

removed_users = "wjaffrey jsoto abernard jhill awilliam"
print("before .split():", removed_users)
removed_users = removed_users.split()
print("after .split():", removed_users)

approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
print("before .join():", approved_users)
approved_users = ",".join(approved_users)
print("after .join():", approved_users)
