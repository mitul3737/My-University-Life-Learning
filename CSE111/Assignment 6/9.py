class Student:
    total=0
    bracu_t=0
    other_t=0

    def __init__(self,name,department,uni="BRAC University"):
        self.name=name
        self.department=department
        self.uni=uni
        if self.uni=="BRAC University":
            Student.total+=1
            Student.bracu_t+=1
        else:
            Student.total += 1
            Student.other_t += 1


    @classmethod
    def createStudent(cls,name,dep,uni="BRAC University"):
        return cls(name,dep,uni)

    @classmethod
    def printDetails(cls):
        print(f"Total Student(s): {Student.total}\nBRAC University Student(s): {Student.bracu_t}\nOther Institution Student(s): {Student.other_t}")

    def individualDetail(self):
        print(f"Name: {self.name}\nDepartment: {self.department}\nInstitution: {self.uni}")

Student.printDetails()
print('#########################')
mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()
print('========================')
harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()
print('=========================')
levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()