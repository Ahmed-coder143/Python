
points = []
for _ in range(3):
    x, y = map(int, input("Enter the numbers for three points: ").split())
    points.append((x, y))


x1, y1 = points[0]
x2, y2 = points[1]
x3, y3 = points[2]


slope1 = (y2 - y1) * (x3 - x2)
slope2 = (y3 - y2) * (x2 - x1)


if slope1 == slope2:
    print("The points are collinear: yes")
else:
    print("The points are non-collinear: no")
