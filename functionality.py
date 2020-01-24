'''
Created on 24. jan. 2020

@author: me294
'''


## Loops
# List comprehension
#words   = ["pupsi", "dupsi", "trallala", "the"]
words = "Python's design offers some support for functional programming in the Lisp tradition".split(" ")
lengths = [len(word) for word in words if word!="the"] 
print(words, lengths)

## Functions
# General
def helloWorld():
  print("Hello World")

def nothing():
  pass

def powerOfTwo(pow):
  return 2**pow

helloWorld()
nothing()
a = powerOfTwo(4)
print(a)

# Arguments/parameters
def helloPupsi(pupsi):
  print(pupsi)
  
def helloPupsiDupsi(pupsi,dupsi = "dupsi"):
  print(pupsi + " " + dupsi)
  
helloPupsiDupsi("schupsi","lupsi")
helloPupsiDupsi(dupsi = "lupsi", pupsi = "schupsi") # Will return the same as before.

def helloSomething(*args):
  print("The third word: " + args[2])

def helloSomethingElse(**args):
  print("The pupsi word is: " + args["pupsi"])
  
helloSomething("hello","some","thing")
helloSomethingElse(pupsi="pupsi", dupsi="dupsi")

# Python specials
def factorial(i):
  if i == 0:
    return 1;
  else:
    return i * factorial(i-1)
 
a = factorial(4)
print("The factorial is {}.".format(a))

def formatSomething(func,str):
  func(str)

def firstFormat(str):
  print("One way to format is like this: \"{}\".".format(str))

def secondFormat(str):
  print("\"{}\" could also be formatted like this.".format(str))
  
formatSomething(firstFormat,"pupsi")
formatSomething(secondFormat,"pupsi")

x = lambda a,b,c : a*b*c
d = x(2,3,5)
print(d)