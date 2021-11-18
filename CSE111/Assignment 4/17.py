class Student():
    def __init__(self,*var):


        if var==():
            print("Student name and department need to be set")
        elif len(var)==1:
            print(f"Department for {var[0]} needs to be set")
            self.student_name = var[0]
        elif len(var)==2:
            print(f"{var[0]} is from {var[1]} department")
            self.student_name = var[0]
            self.department = var[1]




    def update_name(self,var_1):
        self.student_name=var_1
    def update_department(self,var_2):
        self.department=var_2

    def enroll(self,*val):
        str_0 =""
        str_1= " "
        lst_1 = []
        str_0 = str(val)  # change sup_pow

        lst_0 = str_0.strip(")(").split(", ")
        self.count=lst_0 #saving list to count itsnumber later


        #making it a string
        for i in range(len(lst_0)):
            if lst_0[i][-1]==", ": #for single values , we have 'x', so, we need x
                str_1 += lst_0[i][1:-2]+', '
            else: #for multiple values we have x, y, z
                str_1 += lst_0[i][1:-1]+', '
        if str_1.strip(" ")[:-1]!=",":
            self.course=str_1.strip(" ")[:-1]
        else:
            self.course=str_1.strip(" ")






    def printDetail(self):
        print(f"Name: {self.student_name}")
        print(f"Department: {self.department}")
        print(f"{self.student_name} enrolled in {len(self.count)} course(s):")

        #solving the issue of ' for 1 value input
        if self.course[-1]=="'": #removing BUS101'
            print(self.course[:-1])
        else:
            print(self.course)




s1 = Student()
print("=========================")
s2 = Student("Carol")
print("=========================")
s3 = Student("Jon", "EEE")
print("=========================")
s1.update_name("Bob")
s1.update_department("CSE")
s2.update_department("BBA")
s1.enroll("CSE110", "MAT110", "ENG091")
s2.enroll("BUS101")
s3.enroll("MAT110", "PHY111")
print("###########################")
s1.printDetail()
print("=========================")
s2.printDetail()
print("=========================")
s3.printDetail()




