#using init()
class Employee:
    def __init__(self):
        self.name="Mitul"

    def displayEmployeeDetails(self):
        print(self.name)


employee_1=Employee()
employee_2=Employee()
employee_1.displayEmployeeDetails()
employee_2.displayEmployeeDetails()
