class Student():
    def __init__(self,name="Unknown",id="X",dept="CSE",d_eff=0):
        self.name=name
        self.id=id
        self.dept=dept
        self.d_eff=d_eff

    def dailyEffort(self,d_eff):
        self.d_eff=d_eff
    def  printDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Department: {self.dept}")
        print(f"Daily Effort: {self.d_eff} hour(s)")
        if self.d_eff<= 2 :
            print('Suggestion: Should give more effort!')
        elif self.d_eff<=4:
            print('Suggestion: Keep up the good work!')
        else:
            print( 'Suggestion: Excellent! Now motivate others.')


harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()