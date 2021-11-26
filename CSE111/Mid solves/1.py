"""Write a Python program that takes multiple words as input from the user and
calculates the frequency of each word. Finally, print all the words (sorted
in ascending order) grouped by frequency (sorted in descending order).
[You can not use built in .count() function]

Sample Input #1:
cow cat cow ant elephant cow dog lion cat goat cow lion tiger elephant

Sample Output #2:
{
4 : ['cow']
2 : ['cat', 'elephant', 'lion']
1 : ['ant', 'dog', 'goat', 'tiger']
}

Sample Input #2:
cat dog lion cat elephant goat cow lion ant tiger elephant cow cow cow

Sample Output #2:
{
4 : ['cow']
2 : ['cat', 'elephant', 'lion']
1 : ['ant', 'dog', 'goat', 'tiger']
}"""






"""Design the required class(es) so that the following expected output is
generated. Do not change any given code. Your code should work for any
number of arguments in the serverPassenger() method."""

class Passenger:
    def __init__(self,name,ticket=None,pay=0):
        self.name=name
        self.ticket=ticket
        self.pay=pay
        if type(self.ticket)==int:
            self.pay=self.ticket
            self.ticket=None


        if self.ticket != None:
            if self.ticket == "Bus Ticket":
                print(f"{self.name} is waiting for Bus having {self.pay} taka in pocket.")
            else:
                print(f"{self.name} is waiting for Train having {self.ticket} taka in pocket.")
        else:
            print(f"{self.name} has {self.pay} taka in pocket.Please buy a ticket.")

    def buyTicket(self,tick):
        self.ticket=tick




class TicketCounter:
    def __init__(self):
        print("This is a general bus and train ticket counter.")
        self.bus_dict={}
        self.train_dict={}
        self.bs_c=0
        self.t_c=0
        self.total=0
    def servePassenger(self,*args):
        fare=args[-1]
        for i in args[:-1]:
            if i.ticket != None:
                if i.ticket == "Bus Ticket":
                    self.bs_c += 1
                    self.total += 1
                    print(f"{i.name} has bought Bus ticket.")
                    self.bus_dict[i.name] = f'Passenger Name:{i.name} Remaining balance:{(i.pay) - 550}'
                else:
                    self.t_c += 1
                    self.total += 1
                    print(f"{i.name} has bought Train ticket.")
                    self.train_dict[i.name] = f'Passenger Name:{i.name} Remaining balance:{(i.pay) - 600}'
            else:
                print(f"{i.name} please buy a ticket first.")

    def showAllPassenger(self):
        print(f"Total passengers:{self.total}")
        print(f"Bus passengers:{self.bs_c}")
        for i in self.bus_dict.keys():
            print(self.bus_dict[i])
        print(f"Train passengers:{self.t_c}")
        for j in self.train_dict.keys():
            print(self.train_dict[j])









# Write you code here
fareChart = {"Bus":550, "Train":600}
p1 = Passenger("Bob", "Bus Ticket",800)
p2 = Passenger("Simon", "Train Ticket", 950)
p3 = Passenger("David", "Train Ticket", 750)
p4 = Passenger("Carol", 1500)
print("1==============================")
tc = TicketCounter()
print("2==============================")
tc.servePassenger(p1,fareChart)
print("3==============================")
tc.servePassenger(p2,fareChart)
print("4==============================")
tc.servePassenger(p3, p4, fareChart)
print("5==============================")
p4.buyTicket("Train Ticket")
tc.servePassenger(p4,fareChart)
print("6==============================")
tc.showAllPassenger()

"""Output:
Bob is waiting for Bus having 800 taka in pocket.
Simon is waiting for Train having 950 taka in pocket.
David is waiting for Train having 750 taka in pocket.
Carol has 1500 taka in pocket.Please buy a ticket.
1==============================
This is a general bus and train ticket counter.
2==============================
Bob has bought Bus ticket.
3==============================
Simon has bought Train ticket.
4==============================
David has bought Train ticket.
Carol please buy a ticket first.
5==============================
Carol has bought Train ticket.
6==============================
Total passengers:4
Bus passengers:1
Passenger Name:Bob Remaining balance:250
Train passengers:3
Passenger Name:Simon Remaining balance:350
Passenger Name:David Remaining balance:150
Passenger Name:Carol Remaining balance:900"""