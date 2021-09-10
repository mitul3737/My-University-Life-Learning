file_1 = open('E:\My University life learning\My-University-Life-Learning\Datacamp\code_2.txt', 'r')
file_2 = open('E:\My University life learning\My-University-Life-Learning\Datacamp\code_2_0.txt', 'w')
string_01 = ""
string_02 = ""
new_list_1 = []
new_list_2 = []
string_01 = file_1.read()
new_list = string_01.split(" ")
for i in range(0, len(new_list)):
    if new_list[i] != "":
        new_list_2.append(new_list[i])

for i in new_list_2:
    string_02 += i + ' '

print(string_02)
file_2.write(string_02)
file_1.close()
file_2.close()