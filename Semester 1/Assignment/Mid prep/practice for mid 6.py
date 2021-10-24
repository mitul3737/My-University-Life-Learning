sum=0
prdt=1
count=0
while True:
    num = input("")
    if num != "Stop":
        sum += int(num)
        prdt *= int(num)
        count += 1
    else:
        break;


print(f"Average : {sum/count}")
print(f"Product: {prdt}")