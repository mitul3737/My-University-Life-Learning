age=int(input(""))
salary=int(input(""))
job=input("")
def calculate_tax(age,salary,job):
    if age<18 or salary <10000 or job=="president":
        print(0)
    elif salary>=10000 and salary<=20000:
        print(salary*(5/100))
    elif salary>20000:
        print(salary*(10/100))

calculate_tax(age,salary,job)