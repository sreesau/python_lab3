#Write a Python program to read a random line from a file.
import random
f=open('text.txt','r')
line=f.readlines()
print(random.choice(line))
f.close()