
class Employee:
    def __init__(self,name,workingPeriod):
        self.name=name
        self.workingPeriod=workingPeriod

    @classmethod
    def employeeByJoiningYear(cls,name,year):
        return cls(name,2021-int(year))

    @staticmethod
    def experienceCheck(workingPeriod,gender):
        if gender=="male":
            if workingPeriod<3:
                return "He is not experienced"
            else:
                return "He is experienced"

        elif gender=="female":
            if workingPeriod<3:
                return "She is not experienced"
            else:
                return "She is experienced"






employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))