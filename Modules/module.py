1)Write a Python program to generate a random color hex, a random alphabetical string, random value between two integers (inclusive) and a random multiple of 7 between 0 and 70. Use random.randint()

import random
import string
print("Generate a random color hex:")
print( "%03x" % random.randint(0, 0xFFF))
print("\nGenerate a random alphabetical string:")
max_length = 25
s = ""
for i in range(random.randint(1, max_length)):
    s += random.choice(string.ascii_letters)
print(s)
print("Generate a random value between two integers, inclusive:")
print(random.randint(0, 10))
print(random.randint(-7, 7))
print(random.randint(1, 1))
print("Generate a random multiple of 7 between 0 and 70:")
print(random.randint(0, 10) * 7)

#output
Generate a random color hex:
ba2

Generate a random alphabetical string:
MIcEYYpYWmm
Generate a random value between two integers, inclusive:
2
-1
1
Generate a random multiple of 7 between 0 and 70:
28


2)Write a Python program to select a random element from a list, set, dictionary-value, and file from a directory. Use random.choice()

import random
# import random
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

#output
Select a random number from a list:
5
1
1

Select a random number from a set:
4
1
4

Select a random value from a dictionary:
1
5
4

Select a random file from a directory.:
boot


3)Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()

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

#output
Construct a seeded random number generator:
0.036293335775877344

Generate a float between 0 and 1, excluding 1:
0.028804607417862393

5) Write a Python program to shuffle the elements of a given list. Use random.shuffle()

import random
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print("Shuffle list:")
print(nums)
words = ['red', 'black', 'green', 'blue']
random.shuffle(words)
print("Shuffle list:")
print(words)

#output
Shuffle list:
[5, 2, 3, 1, 4]
Shuffle list:
['black', 'green', 'blue', 'red']

6)Write a Python program to generate a float between 0 and 1, inclusive and generate a random float within a specific range. Use random.uniform()

import random 
print("Generate a float between 0 and 1, inclusive:")
print(random.uniform(0, 1))
print("\nGenerate a random float within a range:")
random_float = random.uniform(1.0, 3.0)
print(random_float)

#output
Generate a float between 0 and 1, inclusive:
0.4668719546287483

Generate a random float within a range:
2.4474661616018527

7)Write a Python program to create a list of random integers and randomly select multiple items from the said list. Use random.sample()

import random 
print("Create a list of random integers:")
people = range(0, 100)
nums_list = random.sample(people, 10)
print(nums_list)
no_elements = 4
print("\nRandomly select",no_elements,"multiple items from the said list:")
result_elements = random.sample(nums_list, no_elements)
print(result_elements)

#output
Create a list of random integers:
[18, 69, 22, 76, 14, 23, 47, 34, 8, 16]

Randomly select 4 multiple items from the said list:
[8, 22, 23, 18]

8)Write a Python program to set a random seed and get a random number between 0 and 1. Use random.random.

import random 
print("Set a random seed and get a random number between 0 and 1:")
random.seed(0)
new_random_value = random.random()
print(new_random_value)
random.seed(1)
new_random_value = random.random()
print(new_random_value)
random.seed(2)

#output
Set a random seed and get a random number between 0 and 1:
0.8444218515250481
0.13436424411240122

                               DocString
 class school:
    '''Class School'''
  def __init__(self, name, std):
    '''Constructor for class school'''
    self.name = name
    self.std = std
  def disp(self):
    '''Function to display'''
    print(self.name)
    print(self.std)   
help(school.disp)
st = school("Fousia", 10)
print(st.__doc__)   

                               Directory
   
import os 
def current_path(): 
    print("Current working directory before") 
    print(os.getcwd()) 
    print() 
current_path()
os.chdir('../') 
current_path() 

                               Argparse
    
import argparse
parser.add_argument('integers', metavar ='N', type = int, nargs ='+',help ='an integer for the accumulator') 
parser.add_argument(dest ='accumulate', action ='store_const',const = sum,  help ='sum the integers')
args = parser.parse_args()
print(args.accumulate(args.integers))
 
                               Subprocess
        
import subprocess
subprocess.run(["python3","-c", "init.py"])

                                Sysarg

import sys
n = len(sys.argv)
print("Total arguments passed:", n)
print("\nName of Python script:", sys.argv[0])
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")   
Sum = 0
for i in range(1, n):
    Sum += int(sys.argv[i])     
print("\n\nResult:", Sum)

                                Sysstin
    
import sys  
for line in sys.stdin: 
    if 'q' == line.rstrip(): 
        break
    print(f'Input : {line}') 
print("Exit") 
