import math

def area_of_a_triangle(a,b,c):
    semiperimeter = (a + b + c)/2
    area = math.sqrt(semiperimeter*(semiperimeter-a)*(semiperimeter-b)*(semiperimeter-c))
    return area



print(area_of_a_triangle(3,4,5))