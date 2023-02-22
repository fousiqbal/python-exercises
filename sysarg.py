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



import sys
  print(sys.platform)
  
  
  
  import sys
  print(sys.platform)
  
  
  
  import sys
  print(sys.version)
  
  
  
  import sys
  sys.stdout.write("This is a normal message \n")
  sys.stderr.write("This is a error message \n")
