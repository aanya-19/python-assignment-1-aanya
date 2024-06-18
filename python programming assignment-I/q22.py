size=input("enter the size of the list: ")
list=[]
for i in range(0,size):
    el=input("enter the list el: ")
    list.append(el)
    
print("the list is:", list)

print("the maximum value is: ",max(list))
print("the maximum value is: ",min(list))
