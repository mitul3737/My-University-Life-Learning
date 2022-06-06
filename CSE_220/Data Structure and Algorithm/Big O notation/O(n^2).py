#O(n^2)
def print_item(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
        
print_item(10)

print('#Another example')
def print_another(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)

                    
print_another(10)
#This belongs to O(n^3) but what ever multiples by n, we will just use O(n^2).

