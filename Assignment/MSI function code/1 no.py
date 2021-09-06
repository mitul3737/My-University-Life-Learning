def function_name(var):
    str_01 = ""
    str_01 += num_0[0]
    list_0 = []
    for i in range(0, len(num_0)):
        if num_0[i] not in str_01:
            str_01 += num_0[i]
    for i in str_01:
        str_02 = str(ord(i)) + i + str(ord(i))
        list_0.append(str_02)

    return list_0

num_0 = input("")
print(function_name(num_0))
