# Input
points = []
for _ in range(3):
    x, y = map(int, input().split())
    points.append((x, y))

# Check if points lie on the same line
x1, y1 = points[0]
x2, y2 = points[1]
x3, y3 = points[2]

# Check if slopes are equal
slope1 = (y2 - y1) * (x3 - x2)
slope2 = (y3 - y2) * (x2 - x1)

# Output
if slope1 == slope2:
    print('yes')
else:
    print('no')
