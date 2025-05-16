length = float(input("Enter length: "))

def get_perimeter(length):
    perimeter = 2*(length + length)
    print(f"Perimeter of the square: {perimeter}")
    return perimeter

get_perimeter(length)

def get_area(length):
    area = length*length
    print(f"Area of the square: {area}")
    return area

get_area(length)
