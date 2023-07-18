# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

#What is the difference Between Parameter & Arguments?
#SomeVariableName = SomePieceOfInformation
#parameter = argument

#function without params
def greet():
    print("Hello World")
    print("Howdy Y'all")
    print("Hows the weather today?")

#greet()

#function with params
def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"Howdy {name}!")

#greet_with_name("Mike")

def greet_with(name, location):
    print(f"Hello, {name} what is it like in {location}?")

#greet_with("Moe", "Fresno")

#function with named keywords
def greet_keyword_args(name, location):
    print(f"Hello, {name} what is it like in {location}?")

#although the positions are switched this will still
#print the correct message.
greet_keyword_args(location = "London", name = "Jack")