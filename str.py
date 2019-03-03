genome = input()
genome=genome.upper()
gccnt = 0
total = 0
for nucl in genome:
    total+=1
    if nucl =='C' or nucl == 'G':
        gccnt+=1
print(gccnt/total*100)
