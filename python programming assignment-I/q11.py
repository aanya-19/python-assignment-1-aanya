first=0
second=1
size=input("enter the size of fibonacci series: ")
print("the fibbionaci series:")
print(first)
print(second)

for i in range(0,size-2):
    sum=first+second
    print(sum)
    first=second
    second=sum