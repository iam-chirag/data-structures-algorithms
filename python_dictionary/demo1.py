
emp_details = {
    "Name": "Chirag",
    "Age": 25,
    "Salary": 20
}

print(emp_details)
print(len(emp_details))

for key in emp_details:
    print(key)

for value in emp_details.values():
    print(value)

for key, value in emp_details.items():
    print(f"key {key} and value {value}")

del emp_details['Name']

emp_details['Company'] = "Inferenz"

print(emp_details)
print(len(emp_details))

res = True if 'Chirag' in emp_details else False
print(res)
