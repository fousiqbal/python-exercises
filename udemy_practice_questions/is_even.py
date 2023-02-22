def myfunc(*args):
      my_list = []
      for num in args:
        if num % 2 == 0:
            my_list.append(num)
        else:
            pass
      return (my_list)
myfunc(1,2,3,4,5,6,7,8,9)
