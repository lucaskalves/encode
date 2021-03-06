#!/usr/bin/env python

# Copyright (c) 2012 Lucas Kreutz, http://lucaskreutz.com.br/
# See the file license.txt for copying permission.

"""
Encodes a file and decodes if a magic world is given
"""


import sys
import blowfish
import hashlib


class Encode:

    def __init__(self, filename, key):
        # The name of the file that is going to be encoded
        self.filename = filename
        self.key = key
        self.bf = blowfish.Blowfish(key)

    def encode(self):
        """Encodes the given file"""

        # Read the data to encode
        thefile = open(self.filename, 'rb')
        content = thefile.read()
        thefile.close()

        # Encode and save the new data in the file
        self.bf.initCTR()
        encoded = self.bf.encryptCTR(content)

        # Make a hash from the key
        keyhash = hashlib.md5(self.key + "molokosalt")
        encoded += keyhash.hexdigest()

        # Save the file
        thefile = open(self.filename, 'w')
        thefile.write(encoded)
        thefile.close()

        print("I encoded that ~secret~ file... :)")

    def decode(self):
        """Decodes the given file"""

        # Read the data to decode
        thefile = open(self.filename, 'r')
        content = thefile.read()
        thefile.close()

        # take the hash from the key
        keyhash = hashlib.md5(self.key + "molokosalt")

        # Compares if the given key is equal the key given to encode
        if keyhash.hexdigest() == content[len(content) - 32:]:

            # Excludes the hash from the content
            content = content[:len(content) - 32]

            # Decode the data and save it again
            self.bf.initCTR()
            decoded = self.bf.decryptCTR(content)
            thefile = open(self.filename, 'wb')
            thefile.write(decoded)
            thefile.close()

            print("So, that ~secret~ file is decoded... ;)")
        else:

            # You really must watch "A Clockwork Orange"
            print("Whoops. '%s' is not a cool word..." % self.key)


# So, We have work to do
if __name__ == "__main__":

    if len(sys.argv) == 4:
        # Checks if the arguments were given
        filename = sys.argv[1]
        key = sys.argv[2]
        action = sys.argv[3].lower()
        encoder = Encode(filename, key)

        if action == 'd':
            encoder.decode()
        elif action == 'e':
            encoder.encode()
        else:
            print("Hey, '%s' is not a valid action, man." % action)
            print("It's supposed to be 'e' for encode and 'd' for decode")
    else:
        print("Heeey, you should give me a filename, a word and an action...")
        print("\nFile to Encode: The filename of the file")
        print("Secret Word: a word used for encode and decode... min. 8 char.")
        print("Action: e - encode, d - decode")
        print("\nUsage:")
        print("  python encode.py file_to_encode.txt secret_word action")
