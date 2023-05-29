#Write a Python program to append text to a file and display the text.
f=open("text.txt","a")
f.write("\n Python consistently ranks as one of the most popular programming languages.")
f.close()
f=open('text.txt','r')
print(f.read())
f.close()