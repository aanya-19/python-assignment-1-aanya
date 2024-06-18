file_path1='/Users/aanyasingh/Desktop/python programming assignment-I/q5.txt'
try:
    with open(file_path1,'r')as file1:
        read_content=file1.read()
except Exception as e:
    print("error 404")
    
file_path2='/Users/aanyasingh/Desktop/python programming assignment-I/q25.txt'
try:
    with open(file_path2,'w')as file2:
        file2.write(read_content)
        print(read_content, "successfully read and wrote!")
except Exception as e:
    print("error 404")
        