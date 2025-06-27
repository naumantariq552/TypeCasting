# ---------------------------
# Explicit Type Casting Example
# ---------------------------

# Strings '1' and '3' are explicitly converted to float before addition
a = "1"
b = "3"
print(float(a) + float(b))  # Output: 4.0

# ---------------------------
# Integer to Float Conversion
# ---------------------------

a = 12

# Explicitly converting integer to float
f = float(a)
print(f)  # Output: 12.0

# ---------------------------
# Integer to Other Number Systems
# ---------------------------

# Converting to hexadecimal
h = hex(a)
print(h)  # Output: 0xc

# Converting to binary
b = bin(a)
print(b)  # Output: 0b1100

# Converting to octal
o = oct(a)
print(o)  # Output: 0o14

# ---------------------------
# Character to ASCII Conversion
# ---------------------------

# Explicitly converting character to ASCII using ord()
ch = 'c'
char = ord(ch)
print(char)  # Output: 99

# ---------------------------
# ASCII to Character Conversion
# ---------------------------

# Explicitly converting ASCII value to character using chr()
e = 65
n = chr(e)
print(n)  # Output: A


#-------------------------------
#Implicit Type Casting 
#-------------------------------
result = 5 + 2.0  # Python implicitly converts 5 (int) to 5.0 (float)
print(result)     # Output: 7.0



# important Point about implicit type casting is it convert the lower data into highr data type 


#long-double    Higher
#double         Lower than long-double
#float          Lower than double
#long           Lower than float
#int            Lower than long  
#char           Lower