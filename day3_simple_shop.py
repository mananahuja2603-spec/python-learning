item=input("Item name: ")
price=float(input("Price per unit: "))
quantity=int(input("Quantity: "))
total=price*quantity
print("{}, {} & {}=${}".format(item,price,quantity,total))