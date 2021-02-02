## DES is a simple block cipher and  symmetric encryption algorithm
# import the DES library using a customized package
import pyDes
# import this library for generating random number by the system
import os
# getting input text from user
i = input("Enter any string: ")

# Padding function: add ' ' until the string length is multiples of 8
def padded_text(s):
    while len(s)%8 !=0 :
        s += ' '
    return s

p = padded_text(i)

## 

# key should be 8 bytes long.
k_ecb = pyDes.des("DESCRYPT", pyDes.ECB, "\0\0\0\0\0\0\0\0", pad=None, padmode=None)

# encrypted data i.e. in bytes
e_ecb = k_ecb.encrypt(str.encode(p))
print("\n The encrypted string(in bytes) - \n", e_ecb)

# extract the input text from the encrypted input using decryption
d_ecb = k_ecb.decrypt(e_ecb)
print("\n The actual input(in bytes) -  \n", d_ecb)