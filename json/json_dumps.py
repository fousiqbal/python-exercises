import json
python_obj = {
  "name": "John",
  "class":"V",
  "age": 10  
}
print(type(python_obj))
j_data = json.dumps(python_obj)
print(j_data)

