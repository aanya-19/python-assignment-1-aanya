size=input("enter the size of the list: ")
sum=0
list=[]
for i in range(0,size):
    el=input("enter the value")
    list.append(el)
    sum=el+sum
    
print("entered list: ",list)
print("sum: ",sum)
    
