#Type Error, Type Checking and Type Conversion

#Type Errors
#print(len(1234)) #TypeError: object of type 'int' has no len()

#Check types
print(type("123")) #Output: <class 'str'>
print(type(123)) #Output: <class 'int'>

#Type Casting (Changing Data Types)
num = 1234
string = str(num)
flt = float(num)

print(type(num)) #Output: <class 'int'>
print(type(string)) #Output: <class 'str'>
print(type(flt)) #Output: <class 'float'>
