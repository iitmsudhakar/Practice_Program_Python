# Parent class with common attributes
class Player:
    def __init__(self, player_num, name):
        self.player_num = player_num
        self.name = name

    # Common attributes display method
    def display(self):
        print(self.player_num, self.name)


# Child class 1 representing common attributes along with the unique attribute of this child class (goal)
class Fplayer(Player):
    def __init__(self, player_num, name, goals):
        # Referring to the Parent class
        super().__init__(player_num, name)
        self.goals = goals

    # Child 1 attributes display method
    def display(self):
        # Referring to the Parent class
        super().display()
        print(self.goals)


# Child class 2 representing common attributes along with the unique attribute of this child class (runs)
class Cplayer(Player):
    def __init__(self, player_num, name, runs):
        # Referring to the Parent class
        super().__init__(player_num, name)
        self.runs = runs

    # Child 1 attributes display method
    def display(self):
        # Referring to the Parent class
        super().display()
        print(self.runs)


'''
    def goals(self):
        if self.goals > 20:
            print("Star Player")
        else:
            print("Normal Player")
'''

P1 = Fplayer(27, 'Messi', 45)
P2 = Cplayer(7, 'Dhoni', 1012)
P1.display()
P2.display()
# P1.goals()
