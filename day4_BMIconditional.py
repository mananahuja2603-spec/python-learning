weight=float(input("Weight in kg: "))
height=float(input("Height in ft: "))
bmi=weight/(height**2)
if bmi<18.5:
    print("Underweight")
elif bmi<25:
    print("Normal")
elif bmi<30:
    print("Overweight")
else:
    print("Obese")