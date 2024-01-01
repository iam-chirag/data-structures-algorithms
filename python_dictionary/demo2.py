
emp_detail = {"Name": "Chirag", "Age": 25, "Salary": 20}
emp_details = []

for item in range(1, 5):
    emp = emp_detail.copy()
    emp['Name'] = f"Name-{item}"
    emp['Salary'] = item
    emp_details.append(emp)

print(emp_details)

res = next((item for item in emp_details if item['Name'] == "Name-4"), {})
print(res)

res = list(filter(lambda emp: emp['Name'] == 'Name-4', emp_details))
print(res)

new_list = sorted(emp_details, key=lambda d: d['Salary'], reverse=True)
print(new_list)

