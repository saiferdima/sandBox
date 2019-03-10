class_array = {}
cached_exceptions = []
checked_list = []


def parse_command(command):
    if len(command) == 1:
        class_array[command[0]] = []
    else:
        parents = command[1].split(' ')
        class_array[command[0]] = parents
        for cl in parents:
            if cl not in class_array:
                parse_command(cl)


def isParent(first_class, second_class):
    temp = []
    if first_class in class_array[second_class] or first_class == second_class:
        return "Yes"
    elif class_array[second_class] == [] or second_class not in class_array:
        return "No"
    else:
        for cc in class_array[second_class]:
            temp.append(isParent(first_class, cc))
    if "Yes" in temp:
        return "Yes"
    else:
        return "No"


def is_already_checked(e_to_check):
    temp = []
    for ce in cached_exceptions:
        # print("CE = " + str(ce))
        # print("e_to_check = " + str(e_to_check))
        temp.append(isParent(ce,e_to_check))
    # print(temp)
    cached_exceptions.append(e_to_check)
    if "Yes" in temp:
        return True
    else:
        return False


n1 = int(input())
while n1 > 0:
    creation_command = input().split(" : ")
    parse_command(creation_command)
    # print(class_array)
    n1 = n1 - 1
n2 = int(input())
while n2 > 0:
    what_to_check = input()
    if is_already_checked(what_to_check):
        checked_list.append(what_to_check)
    # print(checked_list)
    n2 = n2 - 1
for n in checked_list:
    print(n)
