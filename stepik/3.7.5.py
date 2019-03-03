result = {}
result_string = ''
for i in range(1,12):
    result[str(i)] = '-'
# print(result)
with open('input.txt', 'r') as file:
    for line in file:
        data = line.strip().split('\t')
        if (result[data[0]] == '-'):
            result[data[0]] = float(data[2])
        else:
            result[data[0]] =(float(result[data[0]]) + float(data[2])) / 2

with open('output.txt', 'w') as file:
    for key in result:
        result_string = result_string + (str(key)+ ' '+ str(result[key]) + '\n')

    file.write(result_string)
