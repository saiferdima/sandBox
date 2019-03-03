n1 = int(input())
dictionary = []
errors = []
while n1 > 0:
    dictionary.append(input().lower())
    n1 = n1 - 1
n2 = int(input())

while n2 > 0:
    string = input().lower().split(' ')
    for word in string:
        if word not in dictionary and word not in errors:
            errors.append(word)
    n2 = n2 - 1
for w in errors:
    print(w)
