#learning about algorithm

#extract first 3 digit from a list of ip address tp knopw which netwtrok they belong

#here we use loop string and list

ip = ["192.168.0.1", "172.16.0.3", "201.50.1.5", "250.120.10.20", "198.51.100.2"]
netwrok=[]
for i in ip:
    netwrok.append(i[0:3])
print(netwrok)                                                                    