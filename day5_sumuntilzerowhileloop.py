total=0
num=int(input("Enter number(0 to Stop): "))
while num!=0:
    total=total+num
    num=int(input("Enter number(0 to Stop): "))
print("Total: {}".format(total))
