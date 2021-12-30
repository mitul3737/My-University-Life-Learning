class myList:
    def __init__(self, *args):
        self.list_0 = []
        self.sum_0 = 0

        self.count = 0
        if len(args) != 0:
            for i in args:
                self.list_0.append(int(i))
                self.count += 1
        else:
            self.list_0 = [0]

    def merge(self, *args_0):
        for k in args_0:
            self.list_0.append(k)
            self.count += 1

    def sum(self):
        self.sum_0 = 0
        for j in self.list_0:
            self.sum_0 += j
        print(f"Sum: {self.sum_0}")

    def average(self):
        try:
            print(f"Average: {self.sum_0 / self.count}")
        except ZeroDivisionError:
            print(f"Average: 0")


l1 = myList(2, 3, 4, 5, 6)  # you might need a list inside your class to store the values
l1.sum()
l1.merge(4, 5, 9)
l1.sum()
l1.average()
print("-----------------------------")
l2 = myList()
l2.average()
l2.merge(1, 2, 4, 8)
l2.sum()

"""Sum: 20
Sum: 38
Average: 4.75
-----------------------------
Average: 0
Sum: 15
"""