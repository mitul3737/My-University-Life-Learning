class Wadiya():
    def __init__(self, name, designation, num_of_wife, dictator):
        self.name = 'Aladeen'
        self.designation = 'President Prime Minister Admiral General'
        self.num_of_wife = 100
        self.dictator = True

    def name_1(self, name):
        self.name = name
        print(f'Name of President: {wadiya.name}')

    def designation_1(self, designation):
        self.designation = designation
        print(f'Designation: {wadiya.designation}')

    def num_of_wife_1(self, num_of_wife):
        self.num_of_wife = num_of_wife
        print(f'Number of wife: {wadiya.num_of_wife}')

    def dictator_1(self, dictator):
        self.dictator = dictator
        print(f'Is he/she a dictator: {wadiya.dictator}')


print('Part 1:')
wadiya = Wadiya('Aladeen', 'President Prime Minister Admiral General', 100, 'True')
wadiya.name_1('Aladeen')
wadiya.designation_1('President Prime Minister Admiral General')
wadiya.num_of_wife_1(100)
wadiya.dictator_1('True')
"""print(f'Name of President: {wadiya.name}')
print(f'Designation: {wadiya.designation}')
print(f'Number of wife: {wadiya.num_of_wife}')
print(f'Is he/she a dictator: {wadiya.dictator}')
"""

print('Part 2:')
wadiya = Wadiya('Donald Trump', 'President', 1, 'False')
wadiya.name_1('Donald Trump')
wadiya.designation_1('President')
wadiya.num_of_wife_1(1)
wadiya.dictator_1('False')
"""print(f'Name of President: {wadiya.name}')
print(f'Designation: {wadiya.designation}')
print(f'Number of wife: {wadiya.num_of_wife}')
print(f'Is he/she a dictator: {wadiya.dictator}')"""




