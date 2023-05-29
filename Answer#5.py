#Write a Python program to read a file line by line and store it into a list.
f=open('fruits.txt','r')
lines=f.readlines()
lines=[i.strip() for i in lines]
print(lines)
f.close()