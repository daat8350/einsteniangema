
lenses=[]
radius=0.1

top=10
y0=100.5
x0=400.5
i=0

while len(lenses)<top:
    y0+=60
    x0+=-20
    newpos=[y0, x0]
    lenses.append([radius, newpos])

#print lenses

# Exporting
filename='cosmic_string.txt'
archive=open(filename, 'w')

for i in lenses:
    archive.write(str(i[0]))
    archive.write('\r\n')
    archive.write(str(i[1][0])+ ','+str(i[1][1]))
    archive.write('\r\n')

archive.close()

print "Done"
