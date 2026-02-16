age = int(input("Enter age: "))
if age >= 18:
    print("Can vote: Yes")
    print("Can drive: Yes")
    print("Can drink: Yes")
elif age >= 16:
    print("Can vote: No")
    print("Can drive: Yes")
    print("Can drink: No")
else:
    print("Can vote: No")
    print("Can drive: No")
    print("Can drink: No")