inf = open('file.txt', 'r')
s1 = inf.readline()
s1 = inf.readline()
inf.close

with open('text.txt') as inf:
    s1 = inf.readline().strip()
    s1 = inf.readline()
