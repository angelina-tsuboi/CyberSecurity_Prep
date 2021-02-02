## contains rest of SHA functions excluding SHA 1
import hashlib

## input value to feed into each hashing algorithm
str = "Hello World"

## SHA256 : This hash function belong to hash class SHA-2, the internal block size of it is 32 bits.
result = hashlib.sha256(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA256 is : ") 
print(result.hexdigest()) 
print('\r')

## SHA384 : This hash function belong to hash class SHA-2, the internal block size of it is 32 bits. This is one of the truncated version.
result = hashlib.sha384(str.encode()) 
print("The hexadecimal equivalent of SHA384 is : ") 
print(result.hexdigest()) 
print('\r')

## SHA224 : This hash function belong to hash class SHA-2, the internal block size of it is 32 bits. This is one of the truncated version.
result = hashlib.sha224(str.encode()) 
print("The hexadecimal equivalent of SHA224 is : ") 
print(result.hexdigest()) 
print('\r')

## SHA512 : This hash function belong to hash class SHA-2, the internal block size of it is 64 bits.
result = hashlib.sha512(str.encode()) 
print("The hexadecimal equivalent of SHA512 is : ") 
print(result.hexdigest()) 
print('\r')


## BONUS 

## useful command to genertate SHA hash for text in mac terminal

## echo -n "Hello World" | shasum -a 256
## put whatever text in between quotes