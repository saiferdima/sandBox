input_string = ''
current_count = '0'
i= 0
result = ''
with open ('input.txt','r') as file:
    for line in file:
        input_string = input_string+line.strip()
print(input_string)
while i < (len(input_string)):
    if input_string[i].isalpha() and int(current_count)==0:
        current_symbol = input_string[i]
    if input_string[i].isdigit():
        current_count = current_count + input_string[i]
    else:
        counter = int(current_count)
        while counter > 0:
            result = result + current_symbol
            counter = counter-1
        current_count = '0'
        current_symbol = input_string[i]
    i=i+1
counter = int(current_count)
while counter > 0:
    result = result + current_symbol    
    counter = counter-1
print (result)
print ("current symbol "+current_symbol )
print ("current counter "+current_count )
with open ('output.txt','w') as file2:
    file2.write(result)


