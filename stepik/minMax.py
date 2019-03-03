

av=a
ma=a
mi=a
b = int(input())
if b > ma:
    ma=b
if b<mi:
    mi=b
c = int(input())
if c > ma:
    av = ma
    ma=c
if c<mi:
    av=mi
    mi=c
print(ma)
print(mi)
print(av)
