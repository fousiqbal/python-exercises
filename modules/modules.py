                                         Pre-defined modules

1) import calendar
   print(calendar.month(2023,1))

#output
     January 2023
   Mo Tu We Th Fr Sa Su
                     1
   2  3  4  5  6  7  8
   9 10 11 12 13 14 15
   16 17 18 19 20 21 22
   23 24 25 26 27 28 29
   30 31
  
2)import keyword
    print(keyword.kwlist)
    
#output
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    

                                              DocStrings
    
3)def add_numbers(a,b):

    '''Take 2 arguments
        return sum
    '''
    return a+b
  print(add_numbers(10,5))
  print(add_numbers.__doc__)

#output
    15
    Take 2 arguments
    return sum
    
  
4)import math
  print(math.__doc__)
  print(math.sqrt.__doc__)
  
#output
  This module provides access to the mathematical functions
  defined by the C standard.
  Return the square root of x.
  
                                                  SYS Module
  
5)import sys
  print(sys.platform)
  
#output
linux

6)import sys
  print(sys.copyright)
  
#output
Copyright (c) 2001-2021 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.

7)import sys
  print(sys.version)
  
#output
3.8.10 (default, Nov 14 2022, 12:59:47) 

8)import sys
  sys.stdout.write("This is a normal message \n")
  sys.stderr.write("This is a error message \n")
  
#output
This is a normal message 
This is a error message 

  
