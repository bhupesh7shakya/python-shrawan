# from cal import sum
import os
# os.remove('hello.txt')
# sum(1,2)
name=input('enter file name')
f=open(f"{name}.txt","a")
f.write("\nhello i was append")
# print(f.read()) 
f.close()
