size=input("enter the size of the list: ")
list=[]
for i in range(0,size):
    el=input("enter the list el: ")
    list.append(el)
    
print("the list is:", list)
search=input("enter an element to count its occurence: ")
l=0
for i in range(0,size):
    if list[i]==search:
        l=l+1
        
print("the occurence of the element is: ",l)
