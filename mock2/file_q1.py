f = open('out.csv','r')
for l in f:
    print(l.strip())
f.close()