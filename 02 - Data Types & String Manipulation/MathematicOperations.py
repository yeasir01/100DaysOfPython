#Mathematic Operations

#Addition
print(3 + 5) #output: 8

#Subtraction
print(5 - 3) #output: 2

#Multiplication
print(5 * 3) #output: 15

#Division
print(6 / 3) #output: 2.0 (Will always type cast to float)

#Floored Number
print(6 // 3) #output: 2 (Will only return the whole number and casts as an int instead of float)

#Exponent (Raise to the power of a given number ^4)
print(2 ** 4) #output: 16

#Level of priority when adding various equations use P.E.M.D.A.S.
# Parenthesis ()
# Exponents **
# Multiplications * or Division /
# Addition + or Subtraction -

print(3 * 3 + 3 / 3 - 3) #output: 7.0
print(3 * (3 + 3) / 3 - 3) #output: 3.0

#Rounding
flt_num_1 = round(3.33333)
flt_num_2 = round(3.66666, 2) #example round(Number, DecimalPlaces)

print(flt_num_1) #output 3
print(flt_num_2) #output: 3.67

#Shorthand Operations
score = 31
score += 1 #Same as doing score = score + 1

print(score) #output 32