def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


for x in range(100):
    print(str(x) + ' ' + str(fib(x)))
