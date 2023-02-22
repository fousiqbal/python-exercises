#Write a Python program to create a list of random integers and randomly select multiple items from the said list. Use random.sample()

print("Create a list of random integers:")
people = range(0, 100)
nums_list = random.sample(people, 10)
print(nums_list)
no_elements = 4
print("\nRandomly select",no_elements,"multiple items from the said list:")
result_elements = random.sample(nums_list, no_elements)
print(result_elements)
