import math
def area_circumference_generator(val_1):
    area=math.pi*(val_1)*val_1
    cir=2*math.pi*val_1
    tup=(area,cir)
    val_2,val_3=tup
    print(tup)
    print(f"Area of the circle is {area} and circumference is {cir}")

    return ""

print(area_circumference_generator(float((input("")))))




'''import math
def area_circumference_generator(val_1):
    area=math.pi*(val_1)*val_1
    cir=2*math.pi*val_1
    return area,cir

print(area_circumference_generator(2.5))
ar_1,cir_1=area_circumference_generator(2.5)
print(f"Area of the circle is {ar_1} and circumference is {cir_1}")'''