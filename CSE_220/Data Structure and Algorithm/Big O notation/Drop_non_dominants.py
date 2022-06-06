def print_item(n):
    #O(n^2)
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    #O(n)
    for k in range(n):
        print(k)        
        
print_item(10)


#So, totally O(n^2 + n). But it will be O(n^2)             

