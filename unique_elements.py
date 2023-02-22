def unique_list(lst):
    seen_numbers = []
    for number in lst:
        if number not in seen_numbers():
            
            seen_numbers.append(number)
    return seen_numbers
unique_list([1,1,1,2,2,2,3,4,4,4])

