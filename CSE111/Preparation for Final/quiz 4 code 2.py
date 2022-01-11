"""Design Naruto class and MyHeroAcademia class which inherit from Anime class
so that the following code provides the expected output.
You can not change any of the given code. Do not modify the given parent
class.

Note: add_character() method in both child classes should work for any
number of parameters and assume parameters will be even numbers."""

class Anime:
   def __init__(self, name, rating, genre):
     self.name = name
     self.rating = rating
     self.genre = genre

   def add_character(self, *info):
     pass

   def __str__(self):
     s = f"Name: {self.name}\nRating: {self.rating}\nGenre: {self.genre}"
     return s


# Write your codes here.
class Naruto(Anime):
    dict={}
    def __init__(self,name,rating,genre,year):
        super().__init__(name,rating,genre)
        self.year=year

    def add_character(self, *args):
        for i in range(1, len(args)+1, 2):
            if args[i] not in self.dict.keys():
                self.dict[args[i]] = [args[i-1]]
            else:
                self.dict[args[i]].append(args[i-1])
    def release_year(self):
        return f"Naruto has been released in {self.year}!!!"

    def __str__(self):
        s = "Anime Details:\n"
        s+=super().__str__()
        s+=f"\nRelease Year: {self.year}"
        s+="\nCharacters:"
        for i in self.dict:
            s+=f"\n{i}: {self.dict[i]}"

        return s


class MyHeroAcademia(Anime):
    dict = {}

    def __init__(self, name, rating, genre, year):
        super().__init__(name, rating, genre)
        self.year = year

    def add_character(self, *args):
        for i in range(0, len(args), 2):
            if args[i] not in self.dict.keys():
                self.dict[args[i]] = [args[i+1]]
            else:
                self.dict[args[i]].append(args[i+1])

    def release_year(self):
        return f"{self.name} has been released in {self.year}!!!"

    def season_status(self):
        return f"My Hero Academia has premiered {self.year} seasons!!!"

    def __str__(self):
        s = "Anime Details:\n"
        s += super().__str__()
        s += f"\nRelease Year: {self.year}"
        s += "\nCharacters:"
        for i in self.dict:
            s += f"\n{i}: {self.dict[i]}"

        return s




naruto = Naruto("Naruto", 10, "Adventure Fiction", 2007)
naruto.add_character("Naruto Uzumaki", "Main", "Itachi Uchiha", "Main", "Madara Uchiha", "Anti Hero", "Pain", "Supporting", "Shikamaru Nara", "Supporting")
print('1.------------------------------------')
print(naruto.release_year())
print('2.------------------------------------')
print(naruto)
print('3.====================================')
my_hero_academia = MyHeroAcademia("My Hero Academia", 8, "Superhero Fiction", 5)
my_hero_academia.add_character("Supporting", "Uraraka", "Anti Hero", "Nomu", "Supporting", "Mirio", "Main", "Midoriya", "Main", "Todoroki")
print('4.------------------------------------')
print(my_hero_academia.season_status())
print('5.------------------------------------')
print(my_hero_academia)

"""OUTPUT:
1.------------------------------------
Naruto has been released in 2007!!!
2.------------------------------------
Anime Details:
Name: Naruto
Rating: 10
Genre: Adventure Fiction
Release Year: 2007
Characters:
Main: ['Naruto Uzumaki', 'Itachi Uchiha']
Anti Hero: ['Madara Uchiha']
Supporting: ['Pain', 'Shikamaru Nara']
3.====================================
4.------------------------------------
My Hero Academia has premiered 5 seasons!!!
5.------------------------------------
Anime Details:
Name: My Hero Academia
Rating: 8
Genre: Superhero Fiction
Season Premiered: 5
Characters:
Supporting: ['Uraraka', 'Mirio']
Anti Hero: ['Nomu']
Main: ['Midoriya', 'Todoroki']"""