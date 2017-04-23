"""Write a program that can perform the Caesar Cipher for english messages that
include both upper- and lowercase characters"""

class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        encoder_upper = [None] * 26                # temp array for encryption
        decoder_upper = [None] * 26                # temp array for decryption
        encoder_lower = [None] * 26                # temp array for encryption
        decoder_lower = [None] * 26                # temp array for decryption
        
        for k in range(26):
            encoder_upper[k] = chr((k + shift) % 26 + ord('A'))
            decoder_upper[k] = chr((k - shift) % 26 + ord('A'))
            encoder_lower[k] = chr((k + shift) % 26 + ord('a'))
            decoder_lower[k] = chr((k - shift) % 26 + ord('a'))
        self._forward = []
        self._backward = []
        self._forward.append(''.join(encoder_upper))   # will store as string
        self._forward.append(''.join(encoder_lower))   # will store as string
        self._backward.append(''.join(decoder_upper))  # since fixed
        self._backward.append(''.join(decoder_lower))  # since fixed
        print(self._forward)
        print(self._backward)
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
                msg[k] = code[0][j]                    # replace this character
            if msg[k].islower():
                j = ord(msg[k]) - ord('a')             # index from 0 to 25
                msg[k] = code[1][j]                    # replace this character
        return ''.join(msg)

if __name__ == '__main__':

    cipher = CaesarCipher(3)
    message = "THE Eagle  IS IN pLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)
