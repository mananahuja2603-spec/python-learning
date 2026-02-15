price=float(input("Price: $"))
if price>100:
    discount=price*0.10
    final=price-discount
    print("Discount: ${:.2f}".format(discount))
    print("Final price: ${:.2f}".format(final))
else:
    print("No discount. Total: ${:.2f}".format(price))