parent_key = "Parent"
var_key = "Var"
global_key = "global"
dictionary = {global_key: {parent_key: None, var_key: []}}


def create(name_space, parrent):
    # print("Create name Space = " + name_space + ' in ' + parrent)
    dictionary[name_space] = {parent_key: parrent, var_key: []}
    # print(dictionary)


def add(name_space, var):
    # print("Add " + var + " to " + name_space)
    dictionary[name_space][var_key].append(var)
    # print(dictionary)


def get(name_space, var):
    # print("Get space name for var " + var + " from space " + name_space)
    if var in dictionary[name_space][var_key]:
        return name_space
    elif name_space != global_key:
        return get(dictionary[name_space][parent_key], var)
    else:
        return None


def parseCmd():
    command, name_space, arg = input().lower().split()
    if command == "create":
        create(name_space, arg)
    elif command == "add":
        add(name_space, arg)
    elif command == "get":
        print(get(name_space, arg))
    else:
        print('Wrong input')


n = int(input())
while n != 0:
    parseCmd()
    n = n - 1
