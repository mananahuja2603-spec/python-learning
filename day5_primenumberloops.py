num=int(input("Enter number: "))
is_Prime=True
if num<2:
    is_Prime=False
else:
    for i in range(2,num):
        if num%i==0:
            is_Prime=False
            break
    
if is_Prime:
    print("{} is prime".format(num))
else:
    print("{} is not prime".format(num))