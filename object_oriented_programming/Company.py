
print("COM FILE LOAD")


class Company:

    def __init__(self, company_name, company_no):
        self.company_name = company_name
        self.__company_no = company_no
        print("In company class")

    def get_company_details(self):
        print(f"\nCompany Name: {self.company_name} \nCompany No: {self.__company_no}")

    def get_no(self):
        print(f"Company No: {self.__company_no}")

    def set_company_no(self, company_no):
        self.__company_no = company_no

    def get_company_no(self):
        return self.__company_no
