'''
Created on 31. jan. 2020

@author: me294
'''

try:
  import pupsi
except:
  print("We don't need pupsi right now.")

## Basics of objects and classes.
print("Here are some examples for basic classes.")
class Animal:
  # These are actual class variables
  limbs = 0
  eyes  = 0
  ears  = 0
  #name  = ""
  
  count = 0
  
  #def __init__(self,limbs,eyes,ears):
  def __init__(self,limbs=4,eyes=2,ears=2):
    # These are object attributes
    self.limbs = limbs
    self.eyes  = eyes
    self.ears  = ears
    
    Animal.count += 1
    
  def __str__(self):
    if not hasattr(self,"name"):
      return "This animal has {} limb(s), {} eye(s) and {} ear(s).".format(self.limbs,self.eyes,self.ears)
    else:
      return "The {} has {} limb(s), {} eye(s) and {} ear(s).".format(self.name, self.limbs,self.eyes,self.ears)
  def __repr__(self):
    return "This animal has {} limb(s), {} eye(s) and {} ear(s).".format(self.limbs,self.eyes,self.ears)
  
  def set_name(self,name):
    self.name = name
    
  def moving(self):
    if not hasattr(self,"name"):
      print("The animal is walking.")
    else:
      print("The {} moving.".format(self.name))
      
  @staticmethod
  def noahs_count():
    print("Noah has to board {} animal(s).".format(Animal.count))
    
beast = Animal();
print(beast.limbs, beast.eyes, beast.ears)
print (beast)

spider = Animal(eyes = 8, ears = 0, limbs = 8 )
print(spider)

spider.set_name("Spider")
print(spider)

spider.moving()

tarantula = Animal(eyes = 8, ears = 0, limbs = 8 )
tarantula.name = "Tarantula"
print(tarantula)

del tarantula.eyes
print(tarantula)

del tarantula
print(tarantula)

# Examples for Inheritance
print("")
print("Here are some examples for inheritance.")

class Cat(Animal):
  def __init__(self):
    Animal.__init__(self,2,2,4) # with self
    super().set_name("Cat") # without self
  
  fur_texture = ""
  def set_fur_texture(self,texture):
    self.fur_texture = texture

  def __str__(self):
    str = super().__str__()
    
    if (self.fur_texture):
      str += " Its fur is {}.".format(self.fur_texture)
    return str

  def meow(self):
    print("Meowwwww!")

pus = Cat()
print(pus)

pus.set_fur_texture("fluffy")
print(pus)

pus.meow()

Animal.noahs_count()

# Examples for Exception Handling
print("")
print("Here are some examples for exception handling.")

a = [ 1,2,3,4 ]
try:
  print(a[5])
except TypeError:
  print("You have chosen the wrong type.")
except:
  print("Something went wrong.")
else:
  print("Nothing went wrong.")
finally:
  print("Always clean up, no matter what.")

x = -1
if x < 0:
  raise TypeError("The number cannot be negative.")