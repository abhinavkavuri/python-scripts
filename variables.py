import functools
var1 = 1  # a variable can contain a-z, A-Z, _, and 0-9 only
a_var_containing_# = 1 #illegal variable

memoize=functools.lru_cache
print(memoize)  #assigning functions to variables

x,y,z=range(3)  # returns [0,1,2]
print(x,y,z)
