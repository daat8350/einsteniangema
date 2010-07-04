filename='a.txt'
archive=open(filename, 'r')
it=0
lenses=[]

for line in archive:
    if it%2==0:
        radius=float(line)
    else:
        k=line.split(',')
        k2=[]
        for i in k:
            k2.append(float(i))
        lenses.append([radius,k2])
    it+=1

print lenses
