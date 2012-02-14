#!/usr/bin/env python

"""
Encodes a file and decodes if a magic world is given
"""

import sys
import base64


filename = sys.argv[1]


if len(sys.argv) > 2:
  if "moloko" in sys.argv:
    thefile = open(filename, 'r')
    content = thefile.read()
    thefile.close()
    
    decoded = base64.b64decode(content)
    thefile = open(filename, 'wb')
    thefile.write(decoded)
    thefile.close()
    
    print("So, that ~secret~ file is decoded... ;)")
  else:
    print("Whoops. '%s' is not a cool word..." % sys.argv[2])

else:
  thefile = open(filename, 'rb')
  content = thefile.read()
  thefile.close()
  
  encoded = base64.b64encode(content)
  thefile = open(filename, 'w')
  thefile.write(encoded)
  thefile.close()
  print("I encoded that ~secret~ file... :)")
