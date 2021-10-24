def string_to_list(x):
    num_02 = []
    num_01 = x[1:-1]
    num_01 = num_01.split(", ")
    for i in num_01:
        num_02.append(int(i))
    return num_02