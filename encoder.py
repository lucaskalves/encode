#!/usr/bin/env python

"""
Encodes a file and decodes if a magic world is given
"""

import sys
import base64

thefile = open(sys.argv[1], 'rb')
content = thefile.read()


if len(sys.argv) > 2:
  if "moloko" in sys.argv:
    base64.decode(thefile, thefile)
    print("So, that ~secret~ file is decoded... ;)")
  else:
    print("Whoops. '%s' is not a cool word..." % sys.argv[2])

else:
  base64.encode(thefile, thefile)
  print("I encoded that ~secret~ file... :)")
