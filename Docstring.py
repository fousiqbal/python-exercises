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




def add_numbers(a,b):

    '''Take 2 arguments
        return sum
    '''
    return a+b
  print(add_numbers(10,5))
  print(add_numbers.__doc__)
  
  
  
  import math
  print(math.__doc__)
  print(math.sqrt.__doc__)
