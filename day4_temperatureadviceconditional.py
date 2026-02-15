temp=int(input("Temperaure (Degree C): "))
if temp<0:
    print("Stay inside, its freezing")
elif temp<15:
    print("Wear a jacket")
elif temp<30:
    print("Perfect")
else:
    print("Use sunscreen, its so hot!")