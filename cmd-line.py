'''
Created on 3. feb. 2020

@author: me294
'''

import argparse

def pupsi():
  # positional arguments
  parser = argparse.ArgumentParser("A simple command line script example.")
  parser.add_argument("first", help="First required argument.")
  parser.add_argument("second", help="Second required argument.")
 
  # optional arguments
  parser.add_argument("-n","--name", help="Print out greeting to a person.")
  parser.add_argument("-w","--world", help="Print out hello world statement.") # optional arguments have to start with at least one hypen -
# 
  args = parser.parse_args()
  if args.name:
    print("Hello " + args.name + "!")
  elif args.world:
    print("Hello World!")
  else:
    print(args.first, args.second)
  
if __name__=="__main__":
  #main(sys.argv[1:])
  pupsi()