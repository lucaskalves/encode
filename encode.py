#!/usr/bin/env python

"""
Encodes a file and decodes if a magic world is given
By Lucas Kreutz <lucas@lucaskreutz.com.br>, Feb 2012

www.lucaskreutz.com.br
"""

import sys
import base64


class Encode:

    def __init__(self, filename):
        # The name of the file that is going to be encoded
        self.filename = filename

    def encode(self):
        """Encodes the given file"""

        # Read the data to encode
        thefile = open(self.filename, 'rb')
        content = thefile.read()
        thefile.close()

        # Encode and save the new data in the file
        encoded = base64.b64encode(content)
        thefile = open(self.filename, 'w')
        thefile.write(encoded)
        thefile.close()

        print("I encoded that ~secret~ file... :)")

    def decode(self, secretword):
        """Decodes the given file"""

        if secretword == "moloko":
            # Read the data to decode
            thefile = open(self.filename, 'r')
            content = thefile.read()
            thefile.close()

            # Decode the data and save it again
            decoded = base64.b64decode(content)
            thefile = open(self.filename, 'wb')
            thefile.write(decoded)
            thefile.close()

            print("So, that ~secret~ file is decoded... ;)")
        else:

            # You really must watch "A Clockwork Orange"
            print("Whoops. '%s' is not a cool word..." % secretword)


# So, We have work to do
if __name__ == "__main__":

    if len(sys.argv) > 1:
        # Checks if the filename was given
        filename = sys.argv[1]
        encoder = Encode(filename)

        if(len(sys.argv) > 2):
            #Pased the secret word... So you wanna decode, hmm?
            encoder.decode(sys.argv[2])
        else:
            encoder.encode()
    else:
        print("Heeey, you should give me a filename...")
        print("\nUsage:")
        print("  python encode.py file_to_encode.txt [secretword]")
