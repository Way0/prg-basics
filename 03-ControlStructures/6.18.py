x = int(input("x = "))
y = int(input("y = "))

if x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
elif x > 0 and y < 0:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")
elif x == 0 and y == 0:
    print(f"Point P({x},{y}) is in position (0,0)")
elif x == 0:
    print(f"Point P({x},{y}) is located on the Y axis")
else:
    print(f"Point P({x},{y}) is located on the X axis")
