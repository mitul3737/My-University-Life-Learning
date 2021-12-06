class Student:
    uniName='BRACU'
    def __init__(self,name,id,dept):
        self.name=name
        self.id=id
        self.dept=dept
        print(self.name,"object created")


st1=Student('Alice',15126727,'CSE')
st2=Student('Jahan',17383983,'BBA')
print(Student.uniName)
print(st1.uniName)
