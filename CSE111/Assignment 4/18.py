class Student():
    def __init__(self,name,roll,dept):
        self.name=name
        self.roll=roll
        self.dept=dept


    def details(self):
        return f"Name: {self.name} \nID: {self.roll}   \nDepartment: {self.dept}"

    def advise(self,*val):
        str_0 =""
        str_1=""
        lst_1 = []
        str_0 = str(val)  # change sup_pow
        lst_0 = str_0.strip(")(").split(", ")
        for i in range(len(lst_0)):
            if lst_0[i][-2] == "'":
                lst_1.append(lst_0[i][-2])

            else:
                lst_1.append(lst_0[i][1:-1])
        #print(lst_1)
        #working wiht credit message
        print(f"{self.name}, you have taken {len(lst_0)*3.0} credits.")

        #working with list of courses
        for i in range(len(lst_0)):
            if lst_0[i][-1]==", ": #for single values , we have 'x', so, we need x
                str_1 += lst_0[i][1:-2]+', '
            else: #for multiple values we have x, y, z
                str_1 += lst_0[i][1:-1]+', '
        if str_1.strip(" ")[:-1]!=",":
            self.course=str_1.strip(" ")[:-1]
        else:
            self.course=str_1.strip(" ")

        print(f"List of courses: {self.course}")

        #working with status
        if len(lst_0)<3:
            print(f"Status: You have to take at least {3-len(lst_0)} more course.")
        elif  len(lst_0)>=3 and len(lst_0)<=4:
            print("Status: Ok")
        else:
            print(f"Status: You have to drop at least {len(lst_0)-4} course.")



s1 = Student('Alice','20103012','CSE')
s2 = Student('Bob', '18301254','EEE')
s3 = Student('Carol', '17101238','CSE')
print('##########################')
print(s1.details())
print('##########################')
print(s2.details())
print('##########################')
s1.advise('CSE110', 'MAT110', 'PHY111')
print('##########################')
s2.advise('BUS101', 'MAT120')
print('##########################')
s3.advise('MAT110', 'PHY111', 'ENG102', 'CSE111', 'CSE230')
