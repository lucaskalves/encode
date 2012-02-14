#!/usr/bin/env python

"""
Encodes a file and decodes if a magic world is given
By Lucas Kreutz <lucas@lucaskreutz.com.br>, Feb 2012

www.lucaskreutz.com.br
"""

import sys
import base64

# The name of the file that is going to be encoded
filename = sys.argv[1]

# Passed the awesome word?
if len(sys.argv) > 2:
    # ... and, is it "moloko"?
    if "moloko" in sys.argv:

        # Read the data to decode
        thefile = open(filename, 'r')
        content = thefile.read()
        thefile.close()

        # Decode the data and save it again
        decoded = base64.b64decode(content)
        thefile = open(filename, 'wb')
        thefile.write(decoded)
        thefile.close()

        print("So, that ~secret~ file is decoded... ;)")
    else:

        # You really must watch "A Clockwork Orange"
        print("Whoops. '%s' is not a cool word..." % sys.argv[2])

else:
    # No cool word given, so, you want to encode, no?
    # Read the data to encode
    thefile = open(filename, 'rb')
    content = thefile.read()
    thefile.close()

    # Encode and save the new data in the file
    encoded = base64.b64encode(content)
    thefile = open(filename, 'w')
    thefile.write(encoded)
    thefile.close()

    print("I encoded that ~secret~ file... :)")
