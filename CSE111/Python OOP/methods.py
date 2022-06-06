class Employee:
    def employeeDetails(self):
        self.name="Mitul"
    @staticmethod
    def WelcomeMessage():
        print("Welcome to our company")

employee=Employee()
employee.employeeDetails()
print(employee.name)
employee.name="Mouly"
print(employee.name)
employee.WelcomeMessage()
