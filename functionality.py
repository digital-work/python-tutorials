'''
Created on 24. jan. 2020

@author: me294
'''

## Conditions / If statements
print("\n**Showing conditions / if statement examples from here out on**")
a=1
if a>0:
  print("{} is greater than 0.".format(a))
else:
  print("{} is not greater than 0.".format(a))
  
a = -1
print("{} is greater than 0.".format(a)) if a>0 else print("{} is not greater than 0.".format(a))
  
a = 0
if a>0:
  print("{} is greater than 0.".format(a))
elif a==0:
  print("{} is equal to 0.".format(a))
elif a == -1:
  pass
elif a == -2:
  pass
else:
  print("{} is not greater than 0.".format(a))

if a > 2:
  pass
else:
  print("{} is greater than 2.".format(a))

a,b = -1,3
if (a > 0 and b > 0) and a+b == 2: #a < 0, not a > 0
  print("Both {} and {} are greater than 0.".format(a,b))
else:
  print("Either {} or {} are smaller than 0.".format(a,b))

a = 4
if a > 0:
  print("{} is greater than 0.".format(a))
  if (a % 2 != 0):
    print("{} is also an uneven number.".format(a))
else:
  print("{} is smaller than 0.".format(a))
  if (a % 2 != 0):
    print("{} is also an uneven number.".format(a))

## Loops
print("\n**Showing loop examples from here out on**")

# While loops
print("\n* While loops *")
print("\nFirst loop")
i = 0
while i < 10:
  i += 1
  print(i)

print("\nSecond loop")
i = 0
while i < 10:
  i += 1
  if i == 5:
    break
  print(i)

print("\nThird loop")
i = 0
while i < 10:
  i += 1
  if i % 2 == 0:
    continue
  print(i)

print("\nFourth loop")
i = 0
while i < 10:
  print(i)
  i += 1
else:
  print("we are exiting the while loop")

# For loops
print("\n* For loops *")
print("\nFirst loop")
for i in  [1,2,3,4,5,6,7]:
  print(i)
for i in "pupsi":
  print(i)

print("\nSecond loop")
for i in "pupsidupsi":
  if i == "u" or i =="i":
    continue
  if i == "d":
    break
  print(i)
else:
  print("Exiting for loop")

print("\nThird loop")
for i in range(10):
  print(i) 
print("\nNext loop")
for i in range(10,23,4): # Printing from 10 to 23-1
  print(i)

for i in "pupsi":
  pass

print("\nFourth loop")
for x in [1,2,3,4,5,6,7]:
  y = 1
  while y < 7:
    print(x,y)
    y +=1

# List comprehension
print("\nList comprehension")
#words   = ["pupsi", "dupsi", "trallala", "the"]
words = "Python's design offers some support for functional programming in the Lisp tradition".split(" ")
if "the" in words:
  print("\n the is in the sentence")
print(words)
lengths = [len(word) for word in words if word!="the"]

a = []
for word in words:
  if (word != "the"):
    a.append(len(word))
print(words,lengths)
print(a)

## Functions
print("\n**Showing function examples from here out on**")
# General
def helloWorld():
  print("Hello World")

def nothing():
  pass

def powerOfTwo(pow):
  if pow == 0:
    return "Zero"
  else: 
    return 2**pow

helloWorld()
nothing()
print(powerOfTwo(4))
print(powerOfTwo(0))

# Arguments/parameters
def helloPupsi(pupsi):
  print(pupsi)
  
def helloPupsiDupsi(pupsi,dupsi = "dupsi"):
  print(pupsi + " " + dupsi)

helloPupsiDupsi("lupsi")
helloPupsiDupsi("schupsi","lupsi")
helloPupsiDupsi(dupsi = "lupsi", pupsi = "schupsi") # Will return the same as before.

def helloSomething(*args):
  if len(args) > 2:
    print("The third word: " + args[2])

def helloSomethingElse(**args):
  if "pupsi" in args:
    print("The pupsi word is: " + args["pupsi"])
  
helloSomething("hello","some")
helloSomethingElse(dupsi="dupsi")

# Python specials
def factorial(i):
  if i == 0:
    return 1;
  else:
    return i * factorial(i-1)
 
a = factorial(4)
print("The factorial is {}.".format(a)) # n!

def formatSomething(func,str):
  func(str)

def firstFormat(str):
  print("One way to format is like this: \"{}\".".format(str))

def secondFormat(str):
  print("\"{}\" could also be formatted like this.".format(str))
  
formatSomething(firstFormat,"pupsi")
formatSomething(secondFormat,"pupsi")
formatSomething("dupsi", "pupsi")

print("\nLambda examples")
x = lambda a,b,c : a*b*c
d = x(2,3,5)
print(d)

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

print("\nPartial functions")
def power(base,exp):
  return base**exp

from functools import partial
power_of_two = partial(power,2)
print(power_of_two(3))

square = partial(power,exp=2)
print(square(7))