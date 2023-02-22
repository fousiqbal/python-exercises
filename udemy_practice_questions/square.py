def square(nums):
    return nums ** 2
my_nums= [1,2,3,4,5,6,7,8,9,10]
for item in map(square, my_nums):
    print(item)
