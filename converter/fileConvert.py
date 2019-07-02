
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
    temp_element = temp_element + line[line.find('(')+1: line.find('))')] + ')'   
    return temp_element


#this.linkToVehicles = element.all(by.xpath("//a[contains(@ng-click, '$ctrl.goToVehicle')]"));
#this.linkToVehicles = buildElements('linkToVehicles', 'xpath' ,"//a[contains(@ng-click, '$ctrl.goToVehicle')  
with open ('input.txt','r') as file:
    for line in file:
        if line.find('= element')>0:
            input_string = input_string+line.strip()
            input_string = input_string+'\n'
            print (newFormat(line))
            result = result + '\n'+ newFormat(line)


with open ('output.txt','w') as file2:
    file2.write(result)
    



    

