a=[int(i) for i in input().split()]
n = int(input())
b = []

for i in range(len(a)):
    if n ==a[i]:
        b.append(i)

if len(b)==0:
    print('Отсутствует')
else:
    for k in b:
        print(k,end=' ')
