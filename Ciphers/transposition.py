
## splits word segments of length at a time into an array
## eg. ("hello", 2) -> ['he', 'll', 'o'] (2 segs at a time)
def split_len(seq, length):
   return [seq[i:i + length] for i in range(0, len(seq), length)]

## order is a mapped value of key (eg. "3214" -> {3: 0, 2: 1, 1: 2, 4:3})
def encode(key, plaintext):
   order = {
      int(val): num for num, val in enumerate(key)
   }
ciphertext = ''


## loops through numbers in sorted version of orders (eg. {3: 0, 2: 1, 1: 2, 4: 3} -> [1,2,3,4])
## then loops through indexes of split_len of the key length (eg. "3214" -> 4)
for index in sorted(order.keys()):
   for part in split_len(plaintext, len(key)):
      try:
        ciphertext += part[order[index]]
      except IndexError:
            continue
   return ciphertext
print(encode('3214', 'HELLO'))

print(encode("3214", "HELLO"))