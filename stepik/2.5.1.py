a=[int(i) for i in input().split()]

b=[]
i=0
l=len(a)

while i < (len(a)):
    if (len(a)==1):
        b.append(a[i])
    elif (i==0):
        b.append(a[l-1]+a[i+1])
    elif (i==l-1):
        b.append(a[i-1]+a[0])
    else:
        
        b.append(a[i-1]+a[i+1])
    i+=1    
for j in b:
    print(j,end=' ')
