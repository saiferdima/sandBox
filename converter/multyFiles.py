import os
import fileConvert
directory = "C:/RIA/OEM-Automation/paccar_support_oem_protractor/pages"
directory_out = 'c:/DL/newFormatPages/'
input_string = ''
result = ''




    
print(os.listdir(directory))
for filename in os.listdir(directory):  
    file =  open (os.path.join(directory,filename),'r')
    for line in file:
        if line.find('= element')>0:
            input_string = input_string+line.strip()
            input_string = input_string+'\n'
            print (fileConvert.newFormat(line))
            result = result + '\n'+ fileConvert.newFormat(line)


    file2 =  open (os.path.join(directory_out,filename),'w+')
    file2.write(result)
    result = ''
    file2.close()
    



    

