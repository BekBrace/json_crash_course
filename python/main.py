import json
# json.load(f): Loads JSON data from a file
# json.loads(s): Loads JSON data from a  string
# json.dump(f) : write JSON object to a file
# json.dumps(s) : will output a JSON object as string

# 1 LOADS()
apple_json = '{"name": "apple", "color": ["red", "green"], "Price": "$ 3.45"}'
apple_dict = json.loads(apple_json)
# print(apple_dict)
# print(apple_dict['name'])
# 2 LOAD()
with open('microsoft.json', 'r') as file:
    data = json.load(file)
# print(data['name'])
# print(data['Foundation']['Founder'])
# 3 DUMPS()
employee = {'id': '07', 'name': 'Mina', 'department': 'Production'}
json_obj = json.dumps(employee, indent=4)
print(json_obj)

# 4 DUMP
employee = {'id': '07', 'name': 'Mina', 'age': 35,
            'height': 179.6, 'department': 'Production'}
with open('employees.json', 'w') as outfile:
    json.dump(employee, outfile)
