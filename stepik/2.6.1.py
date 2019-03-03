n = int(input())
m=[]
for i in range(n):
    for j in range(i):
        if (len(m) < n):
            m.append(i)
        else:
            break
for k in m:
    print(k,end=' ')
