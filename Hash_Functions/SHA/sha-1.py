import hashlib 
  
# prints all available algorithms 
print ("The available algorithms are : ", end ="") 
print (hashlib.algorithms_guaranteed) 

# going to use SHA 1
## SHA1 : The 160 bit hash function that resembles MD5 hash in working and was discontinued to be used seeing its security vulnerabilities.
str = "Hello World"

result = hashlib.sha1(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA256 is : ") 
print(result.hexdigest()) 