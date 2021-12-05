import re
#+ matches 1 or more character
print("Matches : ",len(re.findall("a+","a as ape bug")))
print("Matches : ",re.findall("a+","a as ape bug")) # these 3 words have a once at a time