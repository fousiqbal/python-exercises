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
print("json list : ", json_list)
print("json string : ", json_str)
print("json number1 : ", json_num1)
print("json number2 : ", json_num2)
print("json true : ", json_t)
print("json false : ", json_f)
