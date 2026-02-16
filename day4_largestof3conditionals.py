a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
if a >= b and a >= c:
    print("Largest: {}".format(a))
elif b >= a and b >= c:
    print("Largest: {}".format(b))
else:
    print("Largest: {}".format(c))
