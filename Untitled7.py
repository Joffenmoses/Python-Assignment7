Assignment 1

port1={21:'FTP',22:'SSh',23:'telnet',80:'http'}
port2={}
port2.update({v:k for k,v in port1.items()})
print(port2)


Assignment 2

list1=[(1,2),(3,4),(5,6),(4,5)]
list2=[]
def add(a,b):
    n=a+b
    return n
for i in range(len(list1)):
    (a,b)=list1[i]
    list2.append(add(a,b))
print(list2)
    

Assignment 3
    

list1=[(1,2,3),[1,2],['a','hit','less']]
list2=[]
for i in list1:
    for j in i:
        list2.append(j)
print(list2)
