class Department:
    def __init__(self, s):
        self.semester = s
        self.name = "Default"
        self.id = -1

    def student_info(self):
        print("Name:", self.name)
        print("ID:", self.id)

    def courses(self, c1, c2, c3):
        print("No courses Approved yet!")


class CSE(Department):
    def __init__(self, name, id, sem):
        self.name = name
        self.id = id
        self.semester = sem

    def courses(self, c1, c2, c3):
        print("Courses Approved to this CSE student in")
        print(f"{self.semester} semester :")
        print(c1)
        print(c2)
        print(c3)


class EEE(Department):
    def __init__(self, name, id, sem):
        self.name = name
        self.id = id
        self.semester = sem

    def courses(self, c1, c2, c3):
        print("Courses Approved to this EE student in")
        print(f"{self.semester} semester :")
        print(c1)
        print(c2)
        print(c3)


s1 = CSE("Rahim", 16101328, "Spring2016")
s1.student_info()
s1.courses("CSE110", "MAT110", "ENG101")
print("==================")
s2 = EEE("Tanzim", 18101326, "Spring2018")
s2.student_info()
s2.courses("Mat110", "PHY111", "ENG101")
print("==================")
s3 = CSE("Rudana", 18101326, "Fall2017")
s3.student_info()
s3.courses("CSE111", "PHY101", "MAT120")
print("==================")
s4 = EEE("Zainab", 19201623, "Summer2019")
s4.student_info()
s4.courses("EEE201", "PHY112", "MAT120")

"""
Name: Rahim
ID: 16101328
Courses Approved to this CSE student in
Spring2016 semester :
CSE110
MAT110
ENG101
==================
Name: Tanzim
ID: 18101326
Courses Approved to this EEE student in
Spring2018 semester :
Mat110
PHY111
ENG101
==================
Name: Rudana
ID: 18101326
Courses Approved to this CSE student in
Fall2017 semester :
CSE111
PHY101
MAT120
==================
Name: Zainab
ID: 19201623
Courses Approved to this EEE student in
Summer2019 semester :
EEE201
PHY112
MAT120"""