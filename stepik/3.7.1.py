result = {}
def update_score(arr):
    first_team = arr[0]
    second_team = arr[2]
    result[first_team][0] = result[first_team][0] + 1
    result[second_team][0] = result[second_team][0] + 1
    if int(arr[1]) > int(arr[3]):  # first win
        result[first_team][1] = result[first_team][1] + 1
        result[second_team][3] = result[second_team][3] + 1
        result[first_team][4] = result[first_team][4] + 3
        return 1
    if int(arr[1]) < int(arr[3]):  # second win
        result[second_team][1] = result[second_team][1] + 1
        result[first_team][3] = result[first_team][3] + 1
        result[second_team][4] = result[second_team][4] + 3
        return 2
    else:  # draw
        result[first_team][2] = result[first_team][2] + 1
        result[second_team][2] = result[second_team][2] + 1
        result[second_team][4] = result[second_team][4] + 1
        result[first_team][4] = result[first_team][4] + 1
        return 3

def parseString(arr):
    first_team = arr[0]
    second_team = arr[2]
    if first_team not in result:
        result[first_team] = [0, 0, 0, 0, 0]
    if second_team not in result:
        result[second_team] = [0, 0, 0, 0, 0]
    update_score(arr)


n = int(input())

while n > 0:
    match = (input().split(';'))
    parseString(match)
    n = n - 1
for key in result:
    print(key+':', end='')
    for value in result[key]:
        print(value, end=' ')
    print('')
