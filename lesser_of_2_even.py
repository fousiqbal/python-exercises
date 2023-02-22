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
