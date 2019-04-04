a='name'
b="name"
c='''name'''
type(a) #string type

c="myname"
c.index('n')  #returns index of n

"i" in "ipython"  #test for substring

joined="**".join(["my","name","is","ipython"])
print(joined)       #join stings with a delimiter

"1 2 3".split()
"1*2*3".split('*')

escape="\"escape this quotes\"" #   \ is escape character
print(escape)

print("This is {x} text in {python}".format(x="formatted", python="Python"))  # formatting in python

print(bool("")) #empty string is False in python, vice versa
print(bool(c))

x="pithon"
x.replace("i","y")      #replace i with y
