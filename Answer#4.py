#Write a Python program to read last n lines of a file.
N=int(input("Enter Last N line:"))
f=open('text.txt','r')
lines=f.readlines()
for textline in (lines[-N:]):
    print(textline,end='')
f.close()