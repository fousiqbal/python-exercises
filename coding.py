#Q) write a function that computes the volume of a sphere, given its radius

def vol(radius):
     volume = (4/3)*(3.14)*(radius**3)
     return volume
vol(2)

#output
33.49333333333333


#Q) write a function that checks wheather a number is in given range(inclusive of high and low)

def ranges(a,b,c):
    if a in range(b,c+1):
        print(f'{a} is in the range of {b} and {c}')
    else:
              print("not in range")
ranges(2,1,10)

#output
2 is in the range of 1 and 10


#Q) write a python function that accepts a string and calculates the number of uppercase letters and lowercase letters.

def high_low(s):
    
    uppercase = 0
    lowercase = 0
  
    
    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
      
        else:
            pass
            
    print(f'The original string is: {s}')
    print(f'Lowercase count:{lowercase}')
    print(f'Uppercase count:{uppercase}')
   
high_low('stytutudsGDHdUjioJ')

#output
The original string is: stytutudsGDHdUjioJ
Lowercase count:13
Uppercase count:5
  
  
  #Q) write a Python function that takes a list and returns a new list of the unique elements of the first list.

def unique_list(lst):
    seen_numbers = []
    for number in lst:
        if number not in seen_numbers():
            
            seen_numbers.append(number)
    return seen_numbers
unique_list([1,1,1,2,2,2,3,4,4,4])

#output
[1,2,3,4]


#Q) write a python function to multiply all numbers in a list

def multiply(numbers):
    total = 1
    for num in numbers:
        total = total*num
    return total
multiply([2,3,4,5,6,7,8,9,10])

#output
3628800


#Q) write a function to display tic tac toe game


row1 = ['',' ','']
row2 = ['','','']
row3 = ['',' ','']
row2[1] = 'X'
display (row1,row2,row3)

#output
['', ' ', '']
['', 'X', '']
['', ' ', '']


#Q) program to print 5% of ath sum of given integers

def myfunc(a,b):
     return(a+b)*0.05
myfunc(10,30)

#output
2.0

def myfunc(*args):
    return sum(args)*0.05
myfunc(10,20,30,40,50,60,70,80,90,100)


#output
27.5


#Q) write a program to display it in uppercase in even places and lowercase in odd places

def myfunc(word):
   
    result = ""
    index = 0
    for letter in word:
        if index % 2 == 0:
            result += letter.lower()
        else:
            result += letter.upper()
        index += 1
    return result
myfunc("apple")

#output
'aPpLe'


#Q) Write a program to display the lesser of 2 even numbers else return the highest digit

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            result = a
        else:
            result = b
    else:
        if a > b:
            result = a
        else:
            result = b
    return result
lesser_of_two_evens(2,5)

#output
5


#Q) write a program that return true if the words start with same letter else return false 

def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]
animal_crackers("Lion, Lepord")

#output
True


#Q) write a program that returns true if the sum of 2 digits or the digit itself is 20

def makes_twenty(a,b):
    return (a+b)==20 or a==20 or b==20
makes_twenty(20,18)

#output
True


#Q) Write a program to display the first and forth letters of a word in uppercase

def capital(name):
    first_letter = name[0]
    inbetween = name[1:3]
    last_letter = name[3]
    rest = name[4:]
    return first_letter.upper() + inbetween + last_letter.upper() + rest
capital("programming")

#output
'ProGramming'


#Q) Define a function called myfunc that takes in an arbitrary number of arguments, and returns the sum of those arguments.

def myfunc(*args):
    return sum (args)
myfunc(3,58,98,2)

#output
161


#Q) Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only those arguments that are even.

def myfunc(*args):
      my_list = []
      for num in args:
        if num % 2 == 0:
            my_list.append(num)
        else:
            pass
      return (my_list)
myfunc(1,2,3,4,5,6,7,8,9)

#output
[2, 4, 6, 8]



#Q) Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. 

def myfunc(word):
    result = ""
    index = 0
    for letter in word:
        if index % 2 == 0:
            result += letter.lower()
        else:
            result += letter.upper()
        index += 1
    return result
myfunc("missisippi")

#output
'mIsSiSiPpI'


#Q) write a program to return true if two 3's are adjacent, else return false

def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False
has_33([1,3,1,3])

#output
False


#Q) write a program to return a letter 3 times in a word

def paper_doll(text):
    result = ''
    for char in text:
        result+= char*3
    return result
paper_doll("Hello")
paper_doll("Missisippi")

#output
'MMMiiissssssiiisssiiippppppiii'


#Q) write a program to play blackjack

def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c])-10 <= 21:
        return sum([a,b,c])-10
    else:
        return "Bust"
blackjack(5,2,11)

#output
18


#Q) write a program to play spy game
def spy_game(nums):
    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

spy_game([1,2,3,0,4,5,0,6,7])

#output
True


#Q) write a function that takes in a single letter, and returns a 5*5 representation of that letter

def print_big(letter):
    patterns = {1:'*',2:'* *',3:'*   *',4:'******',5:'****',6:' *',7:'  *  ',8:'*    *',9:'*  '}
    alphabet = {'A':[7,3,4,8,8],'B':[5,3,8,3,2,1,2,3,8,3,5]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
print_big('a')

#output
  *  
*   *
******
*    *
*    *


#Q) write function to return square of given numbers

def square(nums):
    return nums ** 2
my_nums= [1,2,3,4,5,6,7,8,9,10]
for item in map(square, my_nums):
    print(item)
    
    #output
    1
4
9
16
25
36
49
64
81
100
