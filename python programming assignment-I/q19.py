input_str=raw_input("ENTER A STRING VALUE: ")
print("original string: ",input_str)
punct='''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for ele in input_str:
    if ele in punct:
        input_str=input_str.replace(ele," ")
        
print("new string is: ", input_str)
        