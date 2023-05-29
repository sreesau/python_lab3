#Write a Python program to write a list to a file.
list=["lotus","jasmine","lilly","rose"]
f=open('flower.txt','w')
for i in list:
    f.write(i+'\n')
f.close()
