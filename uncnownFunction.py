


dictionary = {}
count = int(input())
for i in range(count):
    x = int(input())
    if x in dictionary:
        result = dictionary[x]
    else:
        result=f(x)
        dictionary[x]=result
    print(result)

def main():
    countMe()

if __name__ == "__main__":
    main()