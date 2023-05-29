# Write a Python program to combine each line from first file with the corresponding line in second file.
f=open('text.txt','r')
s=open('flower.txt','r')
fline=f.readlines()
sline=s.readlines()
for i in range(len(fline)):
      merge= fline[i]+sline[i]
      print(merge,end='')
f.close()
s.close()