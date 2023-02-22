#1)Write a Python program to convert JSON data to Python object.

import json
json_obj =  '{ "Name":"John", "Class":"V", "Age":10 }'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\nName: ",python_obj["Name"])
print("Class: ",python_obj["Class"])
print("Age: ",python_obj["Age"]) 
