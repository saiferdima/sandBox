total = 0
total_math = 0.00
total_fiz = 0.00
total_rus = 0.00
result = ''
with open ('input.txt','r') as file:
    for line in file:
        total = total+1
        current = line.strip().split(";")
        total_math = total_math+(float(current[1]))
        total_fiz = total_fiz+(float(current[2]))
        total_rus = total_rus+(float(current[3]))
        student_ovarage = (float(current[1])+float(current[2])+float(current[3]))/3
        print (current)
        print(student_ovarage)
        result = result + str(student_ovarage)+'\n'
result = result + str(total_math/total)+' '+str(total_fiz/total)+' '+str(total_rus/total)
print(total_math/total,end=' ')
print(total_fiz/total,end=' ')
print(total_rus/total,end=' ')
print('\n\n\n')
print(result)
with open ('output.txt','w') as file:
    file.write(result)


        


