file_path='/Users/aanyasingh/Desktop/python programming assignment-I/q5.txt'
try:
    with open(file_path,'r') as file:
        content=file.read()
        print(content)
        
except Exception as e:
    print("an error occured")