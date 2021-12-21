class Football:
    def __init__(self, team_name, name, role):
        self.__team = team_name
        self.__name = name
        self.role = role
        self.earning_per_match = 0

    def get_name_team(self):
        return 'Name: ' + self.__name + ', Team Name: ' + self.__team


class Player(Football):
    def __init__(self, team_name, name, role, goal, match):
        super().__init__(team_name, name, role)
        self.goal = goal
        self.match = match

    def calculate_ratio(self):
        self.ratio = (self.goal / self.match)

    def print_details(self):
        print(super().get_name_team())
        print(
            f"Team Role: {self.role}\nTotal Goal: {self.goal}, Total Played: {self.match}\nGoal Ratio: {self.ratio}\nMatch Earning: {self.goal * 1000 + self.match * 10}K")


class Manager(Football):
    def __init__(self, team_name, name, role, win):
        super().__init__(team_name, name, role)
        self.win = win

    def print_details(self):
        print(super().get_name_team())
        print(f"Team Role: {self.role}\nTotal Win: 25\nMatch Earning: {self.win * 1000}K")


# write your code here
player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()

"""Name: Ronaldo, Team Name: Juventus
Team Role: Striker
Total Goal: 25, Total Played: 32
Goal Ratio: 0.78125
Match Earning: 25320K
----------------------------------
Name: Zidane, Team Name: Real Madrid
Team Role: Manager
Total Win: 25
Match Earning: 25000K"""