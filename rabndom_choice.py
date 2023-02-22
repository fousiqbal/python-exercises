#Write a Python program to select a random element from a list, set, dictionary-value, and file from a directory. Use random.choice()

import random
import os
print("Select a random number from a list:")
numbers = [1, 2, 3, 4, 5]
print(random.choice(numbers))
print(random.choice(numbers))
print(random.choice(numbers))
print("\nSelect a random number from a set:")
numbers = set([1, 2, 3, 4, 5])
# convert to tuple because sets are invalid inputs
print(random.choice(tuple(numbers)))
print(random.choice(tuple(numbers)))
print(random.choice(tuple(numbers)))
print("\nSelect a random value from a dictionary:")
d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
key = random.choice(list(d))
print(d[key])
key = random.choice(list(d))
print(d[key])
key = random.choice(list(d))
print(d[key]) 
print("\nSelect a random file from a directory.:")
print(random.choice(os.listdir("/")))


#Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()

import random
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
