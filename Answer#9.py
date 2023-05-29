#Write a Python program to count the number of lines in a text file.

f=open('text.txt','r')
lines=f.readlines()
count=0
for textline in lines :
    count+=1
print("Number of the line:",count)
f.close()