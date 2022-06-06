class Employee:
    def __init__(self, name, password, salary):
        self._name = name
        self.password = password
        self.salary = salary

    # setting name
    # you can read the name but cannot change it
    @property  # getter method
    def name(self):
        return self._name

    # setting password
    # you cannot see the password
    @property  # getter method
    def password(self):
        raise AttributeError('password not readable')

    # but you can change the password
    @password.setter  # setter method
    def password(self, new_password):
        self._password = new_password

    # setting salary's property and setter
    # you can read the salary
    @property  # getter method
    def salary(self):
        return self._salary

    # you can change the salary
    @salary.setter  # setter method
    def salary(self, new_salary):
        self._salary = new_salary



