class_array = {}


def parse_command(command):
    if len(command) == 1:
        class_array[command[0]] = ['Object']
    else:
        parents = command[1].split(' ')
        class_array[command[0]] = parents
        for cl in parents:
            if cl not in class_array:
                parse_command(cl)


def isParent(first_class, second_class):
    temp = []
    if first_class in class_array[second_class] or first_class == second_class:
        return"Yes"
    elif class_array[second_class] == ['Object'] or second_class not in class_array:
        return "No"
    else:
        for cc in class_array[second_class]:
           temp.append(isParent(first_class, cc))
    if "Yes" in temp:
        return "Yes"
    else:
        return "No"


n1 = int(input())
while n1 > 0:
    creation_command = input().split(" : ")
    parse_command(creation_command)
    # print(class_array)
    n1 = n1 - 1
n2 = int(input())
while n2 > 0:
    get_command = input().split(" ")
    print(isParent(get_command[0], get_command[1]))
    n2 = n2 - 1
