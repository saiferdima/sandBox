result = {}
result_string = ''
spliter = {}
for i in range(1, 12):
    spliter[str(i)] = 0

for i in range(1, 12):
    result[str(i)] = '-'
# print(result)
with open('input.txt', 'r') as file:
    for line in file:
        data = line.strip().split('\t')
        print(data[0])
        if result[data[0]] == '-':
            result[data[0]] = int(data[2])
            spliter[data[0]] = 1
        else:
            result[data[0]] = result[data[0]] + int(data[2])
            spliter[data[0]] = spliter[data[0]] + 1

with open('output.txt', 'w') as file:
    for key in result:
        if result[key] != '-':
            result_string = result_string + (str(key) + ' ' + str(result[key] / spliter[key]) + '\n')
        else:
            result_string = result_string + (str(key) + ' ' + '-' + '\n')

    file.write(result_string)
