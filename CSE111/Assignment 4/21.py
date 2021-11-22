class Hospital:
    def __init__(self,name):
           self.name=name
           self.d_dict={}
           self.p_dict={}
           self.d_count=0
           self.p_count=0

    def addDoctor(self,var):
        self.d_dict[var.d_id]=[var.d_name,var.d_spe]
        self.d_count+=1


    def getDoctorByID(self,val):
        if val in self.d_dict.keys():
            return f"Doctor's ID:{val}\nName:{self.d_dict[val][0]}\nSpeciality:{self.d_dict[val][1]}"

    def addPatient(self,val_1):
        self.p_dict[val_1.p_id]=[val_1.p_name,val_1.p_age,val_1.p_pho]
        self.p_count+=1

    def getPatientByID(self,val_2):
        if val_2 in self.p_dict.keys():
            return f"Patient's ID:{val_2}\nPatient's name:{self.p_dict[val_2][0]}\nAge:{self.p_dict[val_2][1]}\nPhone: {self.p_dict[val_2][2]}"

    def allDoctors(self):
        print("All Doctors")
        print(f"Number of Doctors: {self.d_count}")
        print(self.d_dict)


    def allPatients(self):
        print("All Patients")
        print(f"Number of Patient: {self.p_count}")
        print(self.p_dict)


class Doctor:
    def __init__(self,id,occ,name,spe):
        self.d_id=id
        self.d_occ=occ
        self.d_name=name
        self.d_spe=spe


class Patient:
    def __init__(self,id,occ,name,age,pho):
        self.p_id=id
        self.p_occ=occ
        self.p_name=name
        self.p_age=age
        self.p_pho=pho








h = Hospital("Evercare")
d1 = Doctor("1d","Doctor", "Samar Kumar", "Neurologist")
h.addDoctor(d1)
print("=================================")
print(h.getDoctorByID("1d"))
print("=================================")
p1 = Patient("1p","Patient", "Kashem Ahmed", 35, 12345)
h.addPatient(p1)
print("=================================")
print(h.getPatientByID("1p"))
print("=================================")
p2 = Patient("2p","Patient", "Tanina Haque", 26, 33456)
h.addPatient(p2)
print("=================================")
print(h.getPatientByID("2p"))
print("=================================")
h.allDoctors()
h.allPatients()


"""
=================================
Doctor's ID: 1d
Name: Samar Kumar
Speciality: Neurologist
=================================
=================================
Patient's ID: 1p
Name: Kashem Ahmed
Age: 35
Phone no.: 12345
=================================
=================================
Patient's ID: 2p
Name: Tanina Haque
Age: 26
Phone no.: 33456
=================================
All Doctors:
Number of Doctors: 1
{'1d': ['Samar Kumar', 'Neurologist']}
All Patients:
Number of Patients: 2
{'1p': ['Kashem Ahmed', 35, 12345], '2p':
['Tanina Haque', 26, 33456]} """

