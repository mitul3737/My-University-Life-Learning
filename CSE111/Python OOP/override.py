class Employee:
    def setNumberOfWorkingHours(self):
        self.NumberOfWorkingHours=40

    def displayNumberOfWorkingHours(self):
        print(self.NumberOfWorkingHours)
class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.NumberOfWorkingHours=45
    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours() #accessing the base class methods

employee=Employee()
employee.setNumberOfWorkingHours()
print("Number of working hours of employee: ",end='')
employee.displayNumberOfWorkingHours()
trainee=Trainee()
trainee.setNumberOfWorkingHours()
print("Number of working hours of trainee: ",end='')
trainee.displayNumberOfWorkingHours()
trainee.resetNumberOfWorkingHours()
print("Number of working hours of trainee after reset: ",end='')
trainee.displayNumberOfWorkingHours()