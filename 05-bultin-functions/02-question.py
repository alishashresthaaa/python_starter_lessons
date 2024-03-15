# Write a python program which accepts the radius of a circle from
# user and compute the area
import math

circle_radius = float(input("Please enter the radius of the circle: "))
circle_area = math.pi * (circle_radius ** 2)
print("The area of the circle is:", circle_area)