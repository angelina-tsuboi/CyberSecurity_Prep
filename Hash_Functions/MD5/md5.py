import hashlib

## encoding Hello World using MD5 has function
result = hashlib.md5(b'Hello World') 

## print equivalent byte value
print("The byte equivalent of hash is : ", end ="") 
print(result.digest()) 