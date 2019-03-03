n = int(input())
if (n % 10 == 1 and n%100 != 11):
    print(n, 'программист')
elif (n % 10 in [2, 3, 4] and not n % 100 in [12, 13, 14] ):
    print(n, 'программиста')
else:
    print(n, 'программистов')
