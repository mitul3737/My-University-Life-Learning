"""Design MSc_Student class and MEng_Student class which inherit
Graduate_Student class so that the following code provides the expected
output."""

class Graduate_Student:
     number_of_graduate_students = 0

     def __init__(self, name, credits):
         self.name = name
         self.credits = credits

     def __str__(self):
         s =  "Department: "+self.name+", Course Credits: "+str(self.credits)
         return s

# Write your codes here.
# Do not change the following lines of code.

class MSc_Student(Graduate_Student):
    dict={}
    student=0
    def __init__(self,name,credits):
        self.name=name
        self.credits=credits
        print(f"{name} Students in CSE have to complete {credits} hours for courses.")



    def add_MSc_Student(self,*args):
        for i in range(0,len(args),2):
            self.dict[args[i]]=args[i+1]
            self.student += 1
            Graduate_Student.number_of_graduate_students += 1

    def __str__(self):
        s=super().__str__()
        s+=f"\nTotal Student(s): {self.student}"
        s+="\nStudent details:"
        for i in self.dict:
            s+=f"\nName: {i}, Course Credits remaining: {self.credits-self.dict[i]}"

        return s



class MEng_Student(Graduate_Student):
    dict_0={}
    student=0
    def __init__(self,name,credits):
        self.name=name
        self.credits=credits
        print(f"{name} Students in CSE have to complete {credits} hours for courses.")

    def add_MEng_Student(self,*args):
        for i in range(0,len(args),2):
            self.dict_0[args[i]]=args[i+1]
            self.student += 1
            Graduate_Student.number_of_graduate_students += 1

    def __str__(self):
        s=super().__str__()
        s+=f"\nTotal Student(s): {self.student}"
        s+="\nStudent details:"
        for i in self.dict_0:
            s+=f"\nName: {i}, Course Credits remaining: {self.credits-self.dict_0[i]}"

        return s

p1 = MSc_Student("CSE", 18)
print("=================================")
p1.add_MSc_Student("Daniel", 12,  "Catherine", 18, "Michael", 15)
print("=================================")
print(p1)
print("=================================")
p2 = MEng_Student("CSE", 30)
print("=================================")
p2.add_MEng_Student("Barry", 12, "Sam", 18)
print("=================================")
print(p2)
print("=================================")
print("Total GraduateStudent: ",Graduate_Student.number_of_graduate_students)

"""OUTPUT:
MSc Students in CSE have to complete 18 hours for courses.
=================================
=================================
Department: CSE, Course Credits: 18
Total Student(s): 3
Student details:
Name: Daniel, Course Credits remaining: 6
Name: Catherine, Course Credits remaining: 0
Name: Michael, Course Credits remaining: 3
=================================
MEng Students in CSE have to complete 30 hours for courses.
=================================
=================================
Department: CSE, Course Credits: 30
Total Student(s): 2
Student details:
Name: Barry, Course Credits remaining: 18
Name: Sam, Course Credits remaining: 12
=================================
Total GraduateStudent:  5"""