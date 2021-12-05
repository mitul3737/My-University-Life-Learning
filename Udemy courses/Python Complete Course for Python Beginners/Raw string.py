
import re
string_0="Here is \\stuff"

#we won't get \\stuff here
#print("Find \\stuff : ",re.search("\\stuff",string_0))

#we can now get \\stuff index
#print("Find \\stuff : ",re.search("\\\\stuff",string_0))


#using raw string as r
print("Find \\stuff : ",re.search(r"\\stuff",string_0))