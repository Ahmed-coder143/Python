import cmath

a, b, c = map(int, input("enter the values: ").split())
X = (b**2) - (4*a*c)
x = (-b - cmath.sqrt(X)) / (2*a)
y = (-b + cmath.sqrt(X)) / (2*a)

print("{:.2f}".format(y.real))
print("{:.2f}".format(x.real))
