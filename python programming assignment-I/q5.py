user_input=raw_input("enter your text")
try:
    with open('q5.txt','w') as q5:
        q5.write(user_input)
except Exception as e:
    print("ERROR 404",str(e))