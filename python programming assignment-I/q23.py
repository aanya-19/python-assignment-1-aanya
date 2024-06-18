temp=input("write the temperature: ")
unit=raw_input("c for celsius/ f for farehnite")
if unit=='c':
    ans=1.8*temp + 32
    print("in farehnite: ", ans)
elif unit=='f':
    ans2=(temp-32)*0.5556
    print("in celsius: ",ans2)
    
