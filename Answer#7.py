#Write a Python program to read a file line by line store it into an array.
f=open('fruits.txt','r')
item_array=[]
lines=f.readlines()
for item in lines:
    item_array.append(item.strip())
print(item_array)
f.close()