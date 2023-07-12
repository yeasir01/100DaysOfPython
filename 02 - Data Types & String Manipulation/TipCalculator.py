#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the Tip Calculator!")

bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? ")
people = input("How many people to split the bill? ")

# Convert data types
bill_float = float(bill)
percentage_float = float(tip) / 100
split_int = int(people)

#Calculations
tip_amount = percentage_float * bill_float
bill_and_tip = tip_amount + bill_float
split = round(bill_and_tip / split_int, 2)

print(f"Each person should pay: ${split}")
