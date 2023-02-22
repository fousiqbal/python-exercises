str1 ="python"
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
