# Somethings that can be done in a python list
# https://docs.python.org/3/tutorial/datastructures.html

#Store many related items in order.
fruits = ["apple", "banana", "oraange"]

print("Original:", fruits)

#Return data by from last using index
print(fruits[0]) #output: apple
print(fruits[-1]) #Returns the last item in the list

#overwrite a record
fruits[2] = "orange"

#Add a record to the end of the list
fruits.append("grapes")

#Add a record to the begging of the list
fruits.insert(0, "Alpine Strawberry")

print("Updated List:", fruits)