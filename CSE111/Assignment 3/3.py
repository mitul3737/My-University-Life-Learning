class Wadiya():
    def __init__(self, name, designation, num_of_wife, dictator):
        self.name = 'Aladeen'
        self.designation = 'President Prime Minister Admiral General'
        self.num_of_wife = 100
        self.dictator = True

        self.name = name
        self.designation = designation
        self.num_of_wife = num_of_wife
        self.dictator = dictator

wadiya = Wadiya('Aladeen', 'President Prime Minister Admiral General', 100, 'True')
#subtask 2
print('Part 1:')
#subtask 1
print(f'Name of President: {wadiya.name}')
print(f'Designation: {wadiya.designation}')
print(f'Number of wife: {wadiya.num_of_wife}')
print(f'Is he/she a dictator: {wadiya.dictator}')
address_0 = id(wadiya)

print('Part 2:')
wadiya = Wadiya('Donald Trump', 'President', 1, 'False')
address_1 = id(wadiya)
print(f'Name of President: {wadiya.name}')
print(f'Designation: {wadiya.designation}')
print(f'Number of wife: {wadiya.num_of_wife}')
print(f'Is he/she a dictator: {wadiya.dictator}')
#subtask 4
print("\nSubtask:")
if address_0 != address_1:
    print('previous information lost')
else:
    print('No, changing had no effect on previous value')

"""lis_0=[]
lis_1=[]

class Wadiya():
     def __init__(self,name,designation,num_of_wife,dictator):
         self.name = 'Aladeen'
         self.designation = 'President Prime Minister Admiral General'
         self.num_of_wife = 100
         self.dictator = True

         self.name=name
         self.designation=designation
         self.num_of_wife=num_of_wife
         self.dictator=dictator



print('Part 1:')
wadiya=Wadiya('Aladeen','President Prime Minister Admiral General',100,'True')
print(f'Name of President: {wadiya.name}')
print(f'Designation: {wadiya.designation}')
print(f'Number of wife: {wadiya.num_of_wife}')
print(f'Is he/she a dictator: {wadiya.dictator}')
address_0=id(wadiya)
lis_0.append(wadiya.name)
lis_0.append(wadiya.designation)
lis_0.append(wadiya.num_of_wife)
lis_0.append(wadiya.dictator)

print('Part 2:')
wadiya=Wadiya('Donald Trump','President',1,'False')
print(f'Name of President: {wadiya.name}')
print(f'Designation: {wadiya.designation}')
print(f'Number of wife: {wadiya.num_of_wife}')
print(f'Is he/she a dictator: {wadiya.dictator}')

lis_1.append(wadiya.name)
lis_1.append(wadiya.designation)
lis_1.append(wadiya.num_of_wife)
lis_1.append(wadiya.dictator)

print("\nSubtask:")
if lis_0!=lis_1:
    print('previous information lost')
else:
    print('No, changing had no effect on previous value')
"""

