from random import normalvariate


lenses=[]
radius=0.1

m=100
n=100
top=100

while len(lenses)<top:
    newpos=[normalvariate(250, m/4), normalvariate(200, m/4)]
    lenses.append([radius, newpos])

#print lenses


filename='a.txt'
archive=open(filename, 'w')

for i in lenses:
    archive.write(str(i[0]))
    archive.write('\r\n')
    archive.write(str(i[1][0])+ ','+str(i[1][1]))
    archive.write('\r\n')

archive.close()

print "Done"
