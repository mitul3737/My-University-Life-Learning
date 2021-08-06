num=input("")
result_str=""
for row in range(0,int(num)):
    for column in range(0,int(num)):
        if (((row == 0 or row == int(num)-1) and column >= 0 and column <= int(num)-1) or row+column==int(num)-1):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str)