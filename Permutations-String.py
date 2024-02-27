from itertools import permutations
x=input("enter the string: ")
perm=permutations(x)
for i in perm:
    z=''.join(i)
    print(z)
    