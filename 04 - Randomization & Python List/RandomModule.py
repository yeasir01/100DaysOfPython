import random

#Random integer between 1 - 10
random_int = random.randint(1, 10)
print(random_int)

#Random Float between 0.00 - 1.00 (does not include 1.00 more like .990)
random_float = random.random()
print(random_float)

#Random float between 0 - 5
random_float_2 = random.random() * 5
print(random_float_2)