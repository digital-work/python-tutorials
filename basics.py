'''
Created on 13. jan. 2020

@author: me294
'''

import random
import numpy


def helloWorld():
  print("hello world")

def helloSomething(string):
  print("hello %s" % string)
  
def nothing():
  # do nothing. fill in later.
  pass
  
def delFunction():
  a = [0,1,2,]
  print(a)
  del a[0]
  print(a)
  #a.clear()
  #print(a)
  del a
  print(a)
  
def numbers():
  a = 1
  b = 1.
  c = 1j
  
  d = int(b)
  
  randoms    = random.randrange(11,20)
  random_int = random.randint(11,20)
  print(randoms)
  print(random_int) 
  
def strings():
  a = "First string"
  b = 'Second string'
  c = """Multiple line string,
Here is the other line"""

  print(a)
  print(b)
  print(c)

  print("\"")
  
  print(a[0:5])
  print(a[::-1])
  print("Lenght of the string: " + str(len(a)))
  
  d = "    Without white space   "
  print(d.strip())
  
  e = "PupSIdusI"
  print(e.upper())
  print(e.lower())
  
  f = "This is a sentence"
  print(f.split(" "))
  
  print(f.startswith("This"))
  print("is" in f)
  print(f.endswith("ence"))
  
  print("this is " + "a concatenated " + "string")
  print("this is a {1} string with {0} integer".format(1,"formatted",2,3,4,5,6,7))

def lists():
  a = [1,1,1.,1j, "pupsi", True]
  print(a)
  
  print(len(a))
  
  a.append(2)
  a.remove("pupsi")
  #a.remove(1)
  del a[0]
  print(a)
  
  a.clear()
  print(a)
  
  a = [1,1.,1j, "pupsi", True]
  print("dupsi" in a)
  print("pupsi" in a)
  
  b = list(numpy.arange(0,100))
  print(b)
  print(b[4])
  print(b[2:10])
  print(b[:10])
  print(b[90:])
  print(b[2:52:2])
  print(b[-1])
  
  c = [1,2,3,4,5]
  d = list("pupsi")
  print(c+d)
  
def tuples():
  a = (1,1.,1j, "pupsi", "pupsi",True)
  print(a)
  print(len(a))
  print(a.index("pupsi",1))
  print(a.index("pupsi"))
  
  
def is_not_empty(string):
  if (string):
    return True
  else:
    return False

def booleans():
  a = True #1
  b = False #0
  print(a)
  print(b)
  print(is_not_empty("pupsi"))
  print(is_not_empty(""))
  
def sets():
  a = {1,1.,1j, "pupsi", True}
  print(a)
  
  a.add(2)
  a.remove(1)
  print(a)
  
  a.update({1,2,3,4})
  print(a)
  
  b = {10,11,12}
  print(a.union(b))
  
def dictionaries():
  dict = {1: "pupsi", "dupsi": True, 2.: 2}
  print(dict)
  
  print(dict[1])
  print(dict[2.])
  
  dict[1] = "dupsi"
  print(dict)
  
  if 2. in dict: # previously has_key(key)
    print(dict[2.])
  
  print("Print keys: ")
  for x in dict:
    print(x)
  
  print("Print values: ")
  for x in dict.values():
    print(x)
  
  print("Print keys and values: ")
  for key,val in dict.items():
    print(key)
    print(val) 
    
  del dict["dupsi"] # same as dict.pop("dupsi")
  print(dict)
  
  dict.clear()
  print(dict)
  
  dict2 = { "a" : 1, "b": { "a" : 1, "b" : {"a" : 1, "b" : 2 }}}
  print(dict2)
  
def conditional_test(is_something):
  if is_something==True:
    print("is true")
  else:
    print("is false")

def conditionals():
  a = True
  conditional_test(a)
  a = False
  conditional_test(a)
  
  a = 1
  b = 2
  if a < b:
    print("b is bigger than a")
  else:
    print("a is bigger than b")
    
  print("b is bigger than a") if b>a else print("b is bigger than a") 
  
  if a == b:
    pass
      
  if a < b:
    if a == 1:
      print("a is equal to one")
      
#helloWorld()
#helloSomething("pupsi")
#nothing()

# Comments
"""
a = 1
def func():
  #global a
  a = 2
  global b 
  b = 3
  print("a (local): " + str(a)) # 2
func()
print("a (global): " + str(a)) # 1 
print("b: " + str(b)) # 3
"""

#delFunction()
#numbers()
#strings()
#lists()
#tuples()
#booleans()
#sets()
dictionaries()

#conditionals()