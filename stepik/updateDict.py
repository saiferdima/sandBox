
def update_dictionary(d, key, value):
    if key in d:
        d[key]= d[key]+[value]
    elif key*2 in d:
        d[key*2]=d[key*2]+[value]
    else:
        d[key*2]= [value]


def main():
    y = 1
    d = {}
    while y ==1:


        key = int(input("Введите key: "))
        value = int(input("Введите value"))
        update_dictionary(d,key,value)
        print(d)
        y = int(input("Введите 1 to continue: "))


if __name__ == "__main__":
    main()


