class Person:
    def greet(self):
        print('I am a Person')

class Teacher:
    def greet(self):
        print('I am a Teacher')

class Student:
    def greet(self):
        print('I am a Student')

class TeachingAssistant(Student,Teacher):
    '''or, pass    to see hw it uses Student class and Teacher class'''
    def greet(self):
        print('I am a TeachingAssistant')

x=TeachingAssistant()
x.greet()
print(TeachingAssistant.__bases__) #it means that TeachingAssistant is a aprt of Student and Teacher class
#help(TeachingAssistant) #mro of TeachingAssistant (the process in which the class will work in multiple inheritence)



