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
