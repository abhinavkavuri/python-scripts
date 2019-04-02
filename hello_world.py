#!/usr/bin/python
import sys
word=input('enter some text') #input() allows user to enter value
print("'hello'"+ word +"'world'") # use + for concatenation
print("xyz,"*6) # use * for multiplication
print("5","6","7") # , adds space between strings
print("hello",40,35,end='ending',sep=';')

help('print')

print("hello",file=sys.stdout) #print string to python console

for i in "python":
        print(i,sep=" ",end="->")
