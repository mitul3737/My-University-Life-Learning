class PokemonBasic:
    def __init__(self, name='Default', hp=0, weakness='None', type='Unknown'):
        self.name = name
        self.hit_point = hp
        self.weakness = weakness
        self.type = type

    def get_type(self):
        return 'Main type: ' + self.type

    def get_move(self):
        return 'Basic move: ' + 'Quick Attack'

    def __str__(self):
        return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness


class PokemonExtra(PokemonBasic):
    def __init__(self, name='Default', hp=0, weakness='None', type='Unknown', sec=None, other=None):
        super().__init__(name, hp, weakness, type)
        self.sec = sec
        self.other = other
        self.move = 'Basic move: ' + 'Quick Attack'

    def get_type(self):
        if self.sec == None:
            return 'Main type: ' + self.type


        else:

            return f'Main type: {self.type}, Secondary type: Flying'

    def get_move(self):
        if self.other == None:
            return self.move
        else:
            self.move += '\nOther move: '
            for k in self.other:
                self.move += k + ', '
            return self.move[:-2]


print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())
print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water',
                          'Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())
print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water',
                         'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())