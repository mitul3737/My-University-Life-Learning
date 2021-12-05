
import re

str_0="rat cat mat pat"
regex=re.compile("[cr]at")
print(regex)
str_0=regex.sub("owl",str_0)#starting with [cr] will be replaced with owl
print(str_0)


"""import re
str_0="F.B.I. I.R.S. CIA"
print("Matches :",len(re.findall(".\..\..",str_0)))
print("Matches :",re.findall(".\..\..",str_0))"""



"""import re

#\w is the same as [1-zA-Z0-9]
#\W is the same as [^a-zA-Z0-9]
str_0="412-555-1212"
if re.search("\w{3}-\w{3}-\w{4}",str_0):
    print("It is a phone number")

if re.search("\w{2,20}","Ultraman"):
   print("It is a valid name")"""