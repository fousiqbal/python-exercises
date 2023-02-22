#Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()


import string
print("Generate random alphabetical character:")
print(random.choice(string.ascii_letters))
print("\nGenerate random alphabetical string:")
max_length = 20
s = ""
for i in range(random.randint(1, max_length)):
    s += random.choice(string.ascii_letters)
print(s)
print("\nGenerate alphabetical string of fixed length:")
word = ""
for i in range(20):
    word += random.choice(string.ascii_letters)
print(word)

#output
Generate random alphabetical character:
m

Generate random alphabetical string:
jlME

Generate alphabetical string of fixed length:
rKCxEVPMBagYKHWZlqpc


4)Write a Python program to construct a seeded random number generator, also generate a float between 0 and 1, excluding 1.Use random.random()

import random
print("Construct a seeded random number generator:")
print(random.Random().random())

print("\nGenerate a float between 0 and 1, excluding 1:")
print(random.random())



