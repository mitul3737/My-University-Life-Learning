"""Design the required class(es) so that the following expected output is
generated. Please use the following logic to calculateCost method.
For each main character the cost is 10000
For each supporting character the cost is 5000
You are not allowed to change any given code."""

class Series:
    def __init__(self,name,year,lang="English"):
        self.name=name
        self.year=year
        self.lang=lang
        self.character_list="No characters assigned yet" #solving the no character prob
        self.main_c=[]
        self.supp_c=[]
        self.cost=0


    def calculateCost(self):
        if self.cost==0:
            print("No cost yet as there is no characters")
        else:
            print(f"Total Cost: {self.cost}")


    def printDetail(self):
            print(f"Series Name: {self.name}\nRelease Year: {self.year}\nLanguage: {self.lang}")
            if self.main_c!=[]:
                print("Main Characters(s):")
                for i in self.main_c:
                    print(i)
            if self.supp_c!=[]:
                print("Supporting Characters(s):")
                for j in self.supp_c:
                    print(j)


    def addCharacter(self,ch):
        if self.character_list =="No characters assigned yet": #checking if no value has been assigned or not
            self.character_list=[]
            if ch.char == "Main character":
                self.main_c.append(ch.name)
                self.character_list.append((ch.name, ch.char))
                self.cost += 10000
            else:
                self.supp_c.append(ch.name)
                self.character_list.append((ch.name, ch.char))
                self.cost += 5000
        else: #if any value is assigned
            if ch.char == "Main character":
                self.main_c.append(ch.name)
                self.character_list.append((ch.name, ch.char))
                self.cost += 10000
            else:
                self.supp_c.append(ch.name)
                self.character_list.append((ch.name, ch.char))
                self.cost += 5000





class Character:
     def __init__(self,name,char="Supporting Character"):
         self.name=name
         self.char=char



# Write you code here
sherlock = Series("Sherlock Holmes", 2010)
print("1.============================================")
print(sherlock.character_list)
print("2.============================================")
sherlock.calculateCost()
print("3.============================================")
sherlock.printDetail()
print("4.============================================")
holmes = Character("Sherlock Holmes", "Main character")
watson = Character("James Watson", "Main character")
irene = Character("Irene Adler")
sherlock.addCharacter(holmes)
sherlock.addCharacter(watson)
sherlock.addCharacter(irene)
print("5.============================================")
sherlock.calculateCost()
print("6.============================================")
sherlock.printDetail()
print("7.============================================")
print(sherlock.character_list)
print("8.###############################################")


squid_games = Series("Squid Games", 2021, "Korean")
print("9.============================================")
print(squid_games.character_list)
print("10.============================================")
squid_games.calculateCost()
print("11.============================================")
squid_games.printDetail()
print("12.============================================")
seong = Character("Seong", "Main character")
kang = Character("Kang")
squid_games.addCharacter(seong)
squid_games.addCharacter(kang)
print("13.============================================")
squid_games.calculateCost()
print("14.============================================")
squid_games.printDetail()
print("15.============================================")
print(squid_games.character_list)



"""Output:
1.============================================
No characters assigned yet
2.============================================
No cost yet as there is no characters
3.============================================
Series Name: Sherlock Holmes
Release Year: 2010
Language: English
4.============================================
5.============================================
Total Cost: 25000
6.============================================
Series Name: Sherlock Holmes
Release Year: 2010
Language: English
Main Characters(s):
Sherlock Holmes
James Watson
Supporting Characters(s):
Irene Adler
7.============================================
[('Sherlock Holmes', 'Main character'), ('James Watson', 'Main character'),
('Irene Adler', 'Supporting character')]
8.###############################################
9.============================================
No characters assigned yet
10.============================================
No cost yet as there is no characters
11.============================================
Series Name: Squid Games
Release Year: 2021
Language: Korean
12.============================================
13.============================================
Total Cost: 15000
14.============================================
Series Name: Squid Games
Release Year: 2021
Language: Korean
Main Characters(s):
Seong
Supporting Characters(s):
Kang
15.============================================
[('Seong', 'Main character'), ('Kang', 'Supporting character')]"""