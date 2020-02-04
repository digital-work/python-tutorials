'''
Created on 3. feb. 2020

@author: me294
'''

import sys,getopt

def main(argv):
  """
This is a little example for a simple command line script.
  """
  try:
    opts,args = getopt.getopt(argv,"hp:",["help","print="])
  except getopt.GetoptError:
    print("Something went wrong. You have to choose one of the valid options.")
    sys.exit(2)
    
  for opt, arg in opts:
    if (opt in ("-h","--help")):
      print(main.__doc__)
      #print( "The options are -h, --help for help\n"
      #       "Or -p, --print for printing your own message.")
    elif (opt in ("-p", "--print")):
      txt = arg
      print(txt)
      
    else:  
      print("Hello World!")
  
if __name__=="__main__":
  main(sys.argv[1:])