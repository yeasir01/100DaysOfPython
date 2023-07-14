""" 
You are going to write a program that will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a 
List called names. For this to work, you must enter all the names as names followed by 
comma then space. e.g. name, name, name

Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!
"""

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Method 1 - Using indices
num_of_bankers = len(names)
random_num = random.randint(0, num_of_bankers - 1)

print(f"{names[random_num]} is going to buy the meal today!")


#Method 2 - Easiest & cleanest method.
rand_name = random.choice(names)
print(f"{rand_name} is going to buy the meal today!")