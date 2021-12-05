#creating an exception class
class VoterEligibility(Exception):
    def __init__(self):
        super() # The super() function in Python makes class inheritance more manageable and extensible.

try:
   age="12"
   if age<18:
       raise VoterEligibility
except TypeError:
    print("Age is not numeric")
except VoterEligibility:
   print("Age is less than 18")
else:
   print("Age is greater than or equal 18")
finally:
   print("End of the program")

