#Write a Python program to construct a seeded random number generator, also generate a float between 0 and 1, excluding 1.Use random.random()

import random
print("Construct a seeded random number generator:")
print(random.Random().random())

print("\nGenerate a float between 0 and 1, excluding 1:")
print(random.random())


#Write a Python program to set a random seed and get a random number between 0 and 1. Use random.random.


import random 
print("Set a random seed and get a random number between 0 and 1:")
random.seed(0)
new_random_value = random.random()
print(new_random_value)
random.seed(1)
new_random_value = random.random()
print(new_random_value)
random.seed(2)

