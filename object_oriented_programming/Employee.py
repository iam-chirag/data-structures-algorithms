
from Company import Company


class Employee(Company):

    def __init__(self, emp_id, emp_name, company_name, company_no):
        super().__init__(company_name, company_no)
        self.emp_id = emp_id
        self.emp_name = emp_name
        print("In Employee Class")

    def get_details(self):
        self.get_company_details()
        print(f"Emp Name: {self.emp_name} \nEmp ID: {self.emp_id} \n")

    def get_no(self):
        # super().get_no()
        print(f"Emp No: {self.emp_id} and Company No: {self.get_company_no()}")

    def get_data(self, name1, name2):
        print(f"Hi: {name1}, {name2}")

    def get_data(self, name1):
        print(f"Hi: {name1}")


employee = Employee(1, "Chirag", "Inferenz", 1)
employee.get_details()
employee.set_company_no(2)
employee.get_no()

employee.get_data("a")

print(globals())

klass = globals()["Employee"]
instance = klass(2, "Chirag", "EIC", 2)
instance.get_no()

