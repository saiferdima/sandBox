
input_string = ''
result = ''

def newFormat(line):
    line=line.strip()
    if line.find('this.')==(-1):
        line = line[4:]
    else:
        line = line[5:]
    temp_element = 'this.'+line[:line.find('=')+1]+' buildElement'
    if line.find('.all')>0:
        temp_element = temp_element + 's'        
    temp_element = temp_element + '(\''
    temp_element = temp_element + line[:line.find('=')]
    temp_element = temp_element + "\', \'"
    line = line[line.find('by.')+3:]
    temp_element = temp_element + line[:line.find('(')] + '\' ,'
    temp_element = temp_element + line[line.find('(')+1: line.rfind('))')] + ')'   
    return temp_element

# with open ('input.txt','r') as file:
#     for line in file:
#         if line.find('= element')>0:
#             input_string = input_string+line.strip()
#             input_string = input_string+'\n'
#             print (newFormat(line))
#             result = result + '\n'+ newFormat(line)
#
#
# with open ('output.txt','w') as file2:
#     file2.write(result)
    



    

