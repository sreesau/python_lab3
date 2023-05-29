#Write a Python program to read a file line by line store it into a variable
f=open('fruits.txt','r')
lines=f.readlines()
print(lines)
f.close()