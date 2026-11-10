 ###
    # Calculates the area of a triangle based on the lengths
    # of the triangle's sides

import math

def triangle_area(a,b,c):
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

areavalue = triangle_area(3, 4, 5)
print(areavalue)

areavalue = triangle_area(5, 12, 13)
print(areavalue)

areavalue = triangle_area(7, 24, 25)
print(areavalue)
