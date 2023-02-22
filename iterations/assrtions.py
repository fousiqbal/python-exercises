try:
    num = int(input("Enter a number:"))
    assert num % 2 == 0
    print("The number is even")
    
  except AssertionError:
    print("Please enter even number")
