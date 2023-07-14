
a = 10
b = 15

#True - "and" operation
if a > 9 and b > 9:
    print("Line 5: Evaluates to True because both conditions are true.")

#False - "and" operation
if a > 9 and b > 15:
    print("This block will not run!")
else:
    print("Line 9: Evaluates to False because one of the two conditions returns a False.")

#True - "or" operation
if a > 9 or b > 15:
    print("Line 9: Evaluates to True because at least one of the two conditions returns True.")
else:
    print("This block will not run!")

#True - "not" operation (negation)
if not a == b:
    print("Line 22: Evaluates to True because 10 == 15 returns false, then it is converted to true because of the not operator.")
else:
    print("This block will not run!")

