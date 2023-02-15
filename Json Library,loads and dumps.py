1)Write a Python program to convert JSON data to Python object.

import json
json_obj =  '{ "Name":"John", "Class":"V", "Age":10 }'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\nName: ",python_obj["Name"])
print("Class: ",python_obj["Class"])
print("Age: ",python_obj["Age"]) 

#output
JSON data:
{'Name': 'John', 'Class': 'V', 'Age': 10}

Name:  John
Class:  V
Age:  10
  
2)Write a Python program to convert Python object to JSON data

import json
python_obj = {
  "name": "John",
  "class":"V",
  "age": 10  
}
print(type(python_obj))
j_data = json.dumps(python_obj)
print(j_data)

#output
<class 'dict'>
{"name": "David", "class": "I", "age": 6}

3)Write a Python program to convert Python objects into JSON strings.

import json
python_dict =  {"name": "John", "age": 10, "class":"V"}
python_list =  ["Red", "Green", "Blue"]
python_str =  "Python Json"
python_int =  (1234)
python_float =  (21.34)
python_T =  (True)
python_F =  (False)
json_dict = json.dumps(python_dict)
json_list = json.dumps(python_list)
json_str = json.dumps(python_str)
json_num1 = json.dumps(python_int)
json_num2 = json.dumps(python_float)
json_t = json.dumps(python_T)
json_f = json.dumps(python_F)
print("json dict : ", json_dict)
print("jason list : ", json_list)
print("json string : ", json_str)
print("json number1 : ", json_num1)
print("json number2 : ", json_num2)
print("json true : ", json_t)
print("json false : ", json_f)

#output
json dict :  {"name": "John", "age": 10, "class": "V"}
jason list :  ["Red", "Green", "Blue"]
json string :  "Python Json"
json number1 :  1234
json number2 :  21.34
json true :  true
json false :  false
  
4)Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.

import json
j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
print("Original String:")
print(j_str)
print("\nJSON data:")
print(json.dumps(j_str, sort_keys=True, indent=4))

#output
Original String:
{'4': 5, '6': 7, '1': 3, '2': 4}

JSON data:
{
    "1": 3,
    "2": 4,
    "4": 5,
    "6": 7
}
