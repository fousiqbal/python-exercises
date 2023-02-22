#Write a Python program to shuffle the elements of a given list. Use random.shuffle()

import random
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print("Shuffle list:")
print(nums)
words = ['red', 'black', 'green', 'blue']
random.shuffle(words)
print("Shuffle list:")
print(words)

