#Write a Python program to count the frequency of words in a file.

f=open('text.txt','r')
dic={}
lines=f.read().strip()
words_low=lines.lower()
words=words_low.split()
for word in words :
  if word in dic:
    dic[word]+=1
  else:
     dic[word]=1
for key in list(dic.keys()):
  print(key,":",dic[key])
f.close()