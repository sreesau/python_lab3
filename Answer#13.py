f=open('text.txt','r')
s=open('python.txt','w')
for i in f:
    s.write(i)
f.close()
s.close()