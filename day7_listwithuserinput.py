names = []
for i in range(5):
    name = input("Enter name {}: ".format(i + 1))
    names.append(name)
print("All names:", names)
print("Sorted:", sorted(names))