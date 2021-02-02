
## BINARY XOR operations
#Use the XOR operator ^ between two values to perform bitwise "exclusive or" on their binary representations. When used between two integers, the XOR operator returns an integer.
## compares 110 and 011 -> 101 -> 5
output = 6 ^ 3
print(output)
## compares 1100 and 0101 -> 1001 -> 9
output = 12 ^ 5
print(output)

## BOOLEAN XOR
# When performing XOR on two booleans, True is treated as 1, and False is treated as 0. XOR between two booleans returns a boolean.
# compares one and zero -> one -> True
output = True ^ False
print(output)
# compares one and one -> zero -> False
output = True ^ True
print(output)
