def s(a, *vs, b=10):

    print('a = '+ str(a))
    print("vs = " + str(vs))
    print('b = '+ str(b))
    res = a + b
    for v in vs:
        res += v
    return res

print(s(11, 10, 10))
# print(s(0,0, 31))
# print(s(11, b=20))
# print(s(5, 5, 5, 5, 1))
# print(s(21))
# print(s(11, 10))
# print(s(b=31))
# print(s(b=31, 0))

