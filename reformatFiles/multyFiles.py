import os
directory = "C:/RIA/OEM-Automation/paccar_support_oem_protractor/pages"
directory_out = 'c:/DL/newFormatPages/'
input_string = ''
result = ''

def newFormat(line):
    temp_element = line[:line.find('=')+1]+' buildElement'
    if line.find('.all')>0:
        temp_element = temp_element + 's'        
    temp_element = temp_element + '(\''
    temp_element = temp_element + line[line.find('this.')+5:line.find(' = ')]
    temp_element = temp_element + "\', \'"
    line = line[line.find('by.')+3:]
    temp_element = temp_element + line[:line.find('(')] + '\' ,'
    temp_element = temp_element + line[line.find('(')+1: line.find(')')] + ')'   
    return temp_element


    
print(os.listdir(directory))
for filename in os.listdir(directory):  
    file =  open (os.path.join(directory,filename),'r')
    for line in file:
        if line.find('= element')>0:
            input_string = input_string+line.strip()
            input_string = input_string+'\n'
            print (newFormat(line))
            result = result + '\n'+ newFormat(line)


    file2 =  open (os.path.join(directory_out,filename),'w+')
    file2.write(result)
    file2.close()
    



    

