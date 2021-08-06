x = int(input(""))
sum = 0
num = "1"
while (x > 0):
    sum += int(num)
    num = str(num) + str("1")
    x = x - 1

print(sum)
