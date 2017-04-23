"""Implement a class , Substitution Cipher, with a constructor that takes a string
with 26 uppercase letters in an arbitrary order and uses that for the forward
mapping for encryption (akin to the self._forward string in our Caesar Cipher
class ) you should derive the backward mapping from the forward version"""

import string
from random import shuffle
class SubstitutionCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""
    def __init__(self, forward):
        """Construct Caesar cipher by calculating the decoder when encoder is given"""
        decoder = [None] * 26 
        self._forward = (''.join(forward))   # will store as string

        for i in range(len(forward)):
            i_decoder  = ord(forward[i]) - ord('A')
            decoder[i_decoder] = chr( i + ord('A'))
        self._backward = (''.join(decoder))

    def encrypt(self, message):
        """Return string representing encripted message."""
        return  self._transform(message, self._forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return  self._transform(secret, self._backward)

    def _transform(self, original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')             # index from 0 to 25
                msg[k] = code[j]                    # replace this character
        return ''.join(msg)

if __name__ == '__main__':

    alpha_list = list(string.ascii_uppercase)
    shuffle(alpha_list)
    """The encoding is donde using a random permutation of the alphabet and the
    encoding array is calulated in the class ctor"""
    cipher = SubstitutionCipher(alpha_list)
    message = "THE Eagle  IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)
