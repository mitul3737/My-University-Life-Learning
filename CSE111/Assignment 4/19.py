dict = {}
dict_1 = {}

class Hotel():
    num=0
    num_0=0
    def __init__(self,h_name):
        self.hotel_name=h_name

    @classmethod
    def id_1(cls):
        cls.num=cls.num+1
        return cls.num

    @classmethod
    def id_2(cls):
        cls.num_0=cls.num_0+1
        return cls.num_0

    #stuff
    def addStuff(self,name,age,phone="000"):
        self.name=name
        self.age=age
        self.phone=phone
        self.id=Hotel.id_1()
        dict[self.id]=[]
        dict[self.id].append(self.name)
        dict[self.id].append(self.age)
        dict[self.id].append(self.phone)
        print(f"Staff With ID {self.id} is added")
    def getStuffById(self,val):
        if val in dict.keys():
            return f"Staff  ID: {val} \nName: {dict[val][0]} \nAge: {dict[val][1]} \nPhone no: {dict[val][2]}"



    #guest
    def addGuest(self,name_0,age_0,phone_0="000"):
        self.name=name_0
        self.age=age_0
        self.phone=phone_0
        self.id=Hotel.id_2()
        #self.id=num_0+1
        dict_1[self.id]=[]
        dict_1[self.id].append(self.name)
        dict_1[self.id].append(self.age)
        dict_1[self.id].append(self.phone)
        print(f"Guest With ID {self.id} is added")
    def getGuestById(self,val):
        if val in dict_1.keys():
            return f"Guest  ID: {val} \nName: {dict_1[val][0]} \nAge: {dict_1[val][1]} \nPhone no: {dict_1[val][2]}"



    def allStaffs(self):
        print("All Staffs:")
        mouly=Hotel.id_1()-1
        print(f"Number of Staffs: {mouly}")
        for k in dict.keys():
            print(f"Staff  ID: {k} Name: {dict[k][0]} Age: {dict[k][1]} Phone no: {dict[k][2]}")

    def allGuest(self):
            print("All Guests:")
            mouly_1 = Hotel.id_2() - 1
            print(f"Number of Staffs: {mouly_1}")
            for j in dict_1.keys():
                print(f"Guest  ID: {j} Name: {dict_1[j][0]} Age: {dict_1[j][1]} Phone no: {dict_1[j][2]}")




h = Hotel("Lakeshore")
h.addStuff( "Adam", 26)
print("=================================")
print(h.getStuffById(1))
print("=================================")
h.addGuest('Carol',35,'123')
print("=================================")
print(h.getGuestById(1))
print("=================================")
h.addGuest("Dianal", 32, '431')
print("=================================")
print(h.getGuestById(2))
print("=================================")
h.allStaffs()
print("=================================")
h.allGuest()