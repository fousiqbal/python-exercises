#iterations 

lst = [1,2,3,4,5]
for i in lst:
    print(i)
lst1 = iter(lst)
next(lst1)

#output----> 1

next(lst1)

#output----> 2

next(lst1)

#output----> 3


#Assertions

1)try:
    num = int(input("Enter a number:"))
    assert num % 2 == 0
    print("The number is even")
    
  except AssertionError:
    print("Please enter even number")
    
    #output----->Enter a number:12
                 The number is even
                 
2)assert "Selenium" in "Selenium is for web automation","validation failed"
  print("validation passed")
  
  #output----->validation passed
  OR
  assert "Python" in "Selenium is for web automation","validation failed"
  print("validation passed")
  
  #output---->AssertionError: validation failed
  
3)str1 ="python"
  str2 ="python"
  assert str1 == str2 , "Strings not matching"
  print("validation passed") 
  
  #output----->validation passed
  OR
  str1 = "python"
  str2 = "Python"

  assert str1 == str2 , "Strings not matching"
  print("validation passed")

  #output------->AssertionError: Strings not matching

4)import math
  assert math.sqrt(5)==2,"Value not correct"
  print("passed")
  
  #output----->AssertionError: Value not correct
  
  
