

def calculateUniqeWords():
    inputString = ((input().lower().split( )))
    print(inputString)
    dictionary = {}
    for i in inputString:
        if i in dictionary:
            dictionary[i]=dictionary[i]+1
        else:
            dictionary[i]=1
    for key, value in dictionary.items():
       print (key,value)






def main():
    print("Input string to calculate  words separated by space")
    calculateUniqeWords()




if __name__ == "__main__":
    main()