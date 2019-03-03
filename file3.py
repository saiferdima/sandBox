input_string = ''
top = 0
top_key=''
with open ('input.txt','r') as file:
    for line in file:
        input_string = input_string+line.strip()
dictionary = {}

input_string = (input_string.lower().split( ))
for i in input_string:
    if i in dictionary:
        dictionary[i]=dictionary[i]+1
    else:
        dictionary[i]=1
 
for key, value in dictionary.items():
    if value == top and (key < top_key):
        top_key = key
    if value > top:
        top_key = key
        top = value
    
    
    print (key,value)
result = str(top_key)+' '+str(dictionary[top_key])
print ("RESULT "+result)
with open ('output.txt','w') as file:
    file.write(result)
    
        


