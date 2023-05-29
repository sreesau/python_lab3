#Write a python program to find the longest words.
f=open('text.txt','r')
words=f.read().split()
longestwordlen=len(max(words,key=len))
result=[word for word in words if len(word)==longestwordlen]
print(result)
f.close()