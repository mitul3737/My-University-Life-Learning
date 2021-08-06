letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!', '#', ' ','.','$', '%', '&', '(', ')', '*', '+','^','@','~','`','_','-','+','=','{','}','[',']','|',':',';','"',"'","<",',','>','.','?','/']
val_1=input("")
s_1=0
s_2=0
s_3=0
for x in range(0,len(val_1)):
    if val_1[x] in letters:
        s_1+=1
    elif val_1[x] in numbers:
        s_2+=1
    elif val_1[x] in special:
        s_3+=1

print(f"The numbers of Alphabets : {s_1}")
print(f"The numbers of Numbers: {s_2}")
print(f"The numbers of special characters: {s_3}")