# движение на восток увеличивает первую координату, а на север — вторую.
cord = {"x": 0, "y": 0}


def moves(input):
    if input[0] == "север":
        return ['y', int(input[1])]
    if input[0] == "юг":
        return ['y', -int(input[1])]
    if input[0] == "запад":
        return ['x', -int(input[1])]
    if input[0] == "восток":
        return ['x', int(input[1])]


n1 = int(input())
while n1 > 0:
    command = input().split(' ')
    move = moves(command)
    cord[move[0]] = cord[move[0]] + move[1]
    n1 = n1 - 1
for key in cord:
    print(cord[key], end=' ')
