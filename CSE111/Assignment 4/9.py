class Patient():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def add_Symptom(self,*add_sym):
        str_0=""
        str_1=""
        str_0=str(add_sym)
        lst_0=str_0.strip(")(").split(", ")
        for i in range(len(lst_0)):
            if lst_0[i][-2]=="'":
                str_1+=lst_0[i][1:-2]+","
                str_1 += " "
            else:
               str_1+=lst_0[i][1:-1]+','
               str_1+=" "
        self.add_sym=str_1[:-2]
    def printPatientDetail(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Symptoms: {self.add_sym}")

p1 = Patient("Thomas", 23)
p1.add_Symptom("Headache")
p2 = Patient("Carol", 20)
p2.add_Symptom("Vomiting", "Coughing")
p3 = Patient("Mike", 25)
p3.add_Symptom("Fever", "Headache", "Coughing")
print("=========================")
p1.printPatientDetail()
print("=========================")
p2.printPatientDetail()
print("=========================")
p3.printPatientDetail()
print("=========================")
