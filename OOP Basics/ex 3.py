class Person:
    def __init__(self, name, age):
        self.name = name
        # data validator for age
        if 20 < age < 80:
            self._age = age
        else:
            raise ValueError('Age must be between 20 to 80')

    def display(self):
        print(self.age, self.name)

    def set_age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError('Age must be between 20 to 80')


if __name__ == '__main__':
    p = Person('Mitul', 30)
    p.display()
