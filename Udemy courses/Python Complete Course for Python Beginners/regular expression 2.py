import re
str_0="The ape was at the apex"
for i in re.finditer("ape.",str_0):
    tup_0=i.span() #span returns a tuple
    print(tup_0)

    print(str_0[tup_0[0]:tup_0[1]])#as tup_0 has 2 values (4,8) so, we get from str_0[4] to str_0[8] . Thus ape and later for (19,23) we get apex
"""As we get ape first so , we get 4 index and new word starts from 8th index
the span() returns (4,8) and again we get apex and this we got again (19,23)"""