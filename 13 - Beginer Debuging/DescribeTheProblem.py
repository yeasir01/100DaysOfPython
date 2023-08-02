############DEBUGGING#####################
#uncomment to solve problems, then describe the solution

# # Describe Problem
""" def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function() """
#Problem: Not printing
#range function returns 1-19 so the loop never reaches 20.
#to fix change 20 to 21.

# # Reproduce the Bug
""" from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num]) """
#Problem: Intermittent index out of range error
#dice_num gives a random integer between 1-6, the list only has 6 items and starts with zero index
#therefore the last index is 5, 6 is an out of range number.
#to fix use the len(dice_imgs) - 1 or just change the arguments to 0, 5

# # Play Computer
""" year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.") """
#Problem: When entering 1994 nothing happens.
#there is no condition that meets the criteria for 1994
#add "=" behind the greater than sign to to elif statement


# # Fix the Errors
""" age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.") """
#Problem: 1) indentation error 2)Entering an age into console creates a TypeError 3)prints "You can drive at age {age}"
#Intent the print statement, cast the input from string to int, add an f before string in print statement.

# #Print is Your Friend
""" pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words) """
#Problem: Always prints 0 regardless of which number is used
#word_per_page has a double equals sign which is a comparison operator and not the assignment operator
#remove one of the "=" signs on line 46

# #Use a Debugger
""" def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13]) """
#Problem: Always returns [26]
#Intent line 58 the append function is outside the loop.