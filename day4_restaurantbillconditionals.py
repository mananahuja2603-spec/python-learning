bill=float(input("Bill amount: "))
tip=bill*0.5
total=bill+tip
print("Tip: ${}".format(tip))
print("Total ${:.2f}".format(total))