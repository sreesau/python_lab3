#Write a Python program to remove newline characters from a file.
f=open('text.txt','r')
lines=f.readlines()
lines=[i.rstrip('\n') for i in lines]
print(lines)
f.close()