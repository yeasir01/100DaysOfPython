#Key value pairs
programming_dictionary = {
    "Bug": "An Error in a program that prevents the program from running as expected.",
    "Functions": "A piece of code that you can easily call over an over again.",
}

#retrieving information from list
##print(programming_dictionary["Bug"])

#add a new entry
programming_dictionary["Loop"] = "The action of doing something over and over."
##print(programming_dictionary)

#creating an empty dictionary
empty_dictionary = {}

#edit existing entry else create a new entry
programming_dictionary["Bug"] = "This is a new entry"
##print(programming_dictionary)

#iterating over a dictionary making sure to pass the key to get value
for key in programming_dictionary:
    print(programming_dictionary[key])

#wipe a dictionary by reassigning the dictionary with an empty one
programming_dictionary = {}
##print("Wiped Dictionary: ", programming_dictionary)