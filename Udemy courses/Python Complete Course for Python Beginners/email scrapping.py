
import re

#1to 20 lowercase and uppercase letters, numbers,plus ._%+ (means we can have any letters and _ and % and +)
#An @ symbol
#2 to 20 lowercase and uppercase letters, numbers, plus .- (means that we can have any letter and a - too)
#A period
#2 to 3 lowercase and uppercase letters
emaillist="db@aol.com m@.com @apple.com db@.com +a@max.com  %jola@hmail.com  karim_saheb@gmail.com  karim-raza@gmail.com  hola@gmai-l.com"
print("Email Matches : ",len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,20}",emaillist)))
print("Email Matches : ",re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,20}",emaillist))