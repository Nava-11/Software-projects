import math
# hard code coefficients
a = 1
b = -3
c = 2
# to calculate discriminant
discriminant = b**2 - 4*a*c
# to check the roots
if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The roots are: {root1} and {root2}")
else:
    print("No real roots exist.")