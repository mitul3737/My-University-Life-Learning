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