import math
def volume_sphere():
    radius = float(input("Enter radius: "))
    volume = (4/3)*(3.14)*(math.pow(radius,3))
    print(f"The volume of a sphere is {volume:.3g}")
    return volume

volume_sphere()