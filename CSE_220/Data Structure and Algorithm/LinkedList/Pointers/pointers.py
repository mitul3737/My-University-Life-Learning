#String does not share address
print('-----Example of String-------')
val_1=11
val_2=val_1
print("value 1",val_1)
print("value 2",val_2)
print("After updating val_1")
val_1=23

print("value 1",val_1)
print("value 2",val_2)



#Dictionary shares address 
print("-----Example of Dictinary----")
val_3={"value":2}
val_4=val_3
print("value 1",val_3)
print("value 2",val_4)
print("After updating val_3")
val_1={"value":5}

print("value 1",val_3)
print("value 2",val_4)
