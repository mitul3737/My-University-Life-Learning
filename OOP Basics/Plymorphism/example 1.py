class Car:
    def start(self):
        print('Engine started')
    def move(self):
        print('Car is running')

    def stop(self):
        print('Brales applied')

class Clock:
    def move(self):
        print('Tick Tick Tick')

    def stop(self):
        print('Clock needles stopped')

class Person:
    def move(self):
        print('Person walking')
    def stop(self):
        print('Taking rest')
    def talk(self):
        print('Hello')


car=Car()
clock=Clock()
person=Person()

#this method will run with which instance you call it
def do_something(x):
    x.move()
    x.stop()


# calling with car instance
do_something(car)

#calling with clock instance
do_something(clock)

#calling with person instance
do_something(person)