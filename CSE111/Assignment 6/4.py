
class Travel:
    count=0
    def __init__(self,source,dest):
        self.source=source
        self.dest=dest
        self.time=1
        Travel.count+=1

    def display_travel_info(self):
         return f"Source: {self.source}\nDestination:{self.dest}\nFlight Time:{self.time}:00"


    def set_time(self,time):
        self.time =time

    def set_destination(self,dest_0):
        self.dest= dest_0
    def set_source(self,source_0):
        self.source=source_0

print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)