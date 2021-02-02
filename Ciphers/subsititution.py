import random

alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
key = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'
plaintext = "Hey, this is really fun!"


def makeKey(alphabet):
   alphabet = list(alphabet)
   random.shuffle(alphabet)
   return ''.join(alphabet)

def encrypt(plaintext, key, alphabet):
    # makes dictionary that relate key as alphabet value and value as key value (eg. {a: n})
    keyMap = dict(zip(alphabet, key))
    # loops through plain text, and concatenates to string: the value of each letter from plaintext inside the keyMap (eg. A -> a -> n (from keymap))
    return ''.join(keyMap.get(c.lower(), c) for c in plaintext)

def decrypt(cipher, key, alphabet):
  # makes dictionary that relate key as key value and value as alphabet value (eg. {n: a}) (reverse direction)
    keyMap = dict(zip(key, alphabet))
    ## loops through each letter of cipher, and concatemates to array the alphabet value of the coressponding value for each cipher letter (key) (eg. N -> n -> a (from keymap)) 
    return ''.join(keyMap.get(c.lower(), c) for c in cipher)

cipher = encrypt(plaintext, key, alphabet)
decryptedText = decrypt(cipher, key, alphabet)
print(plaintext)
print(cipher)
print(decryptedText)