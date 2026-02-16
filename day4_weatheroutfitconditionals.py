weather = input("Weather (sunny/rainy/cold): ").lower()
if weather == "sunny":
    print("Wear: T-shirt and sunglasses")
elif weather == "rainy":
    print("Wear: Raincoat and boots")
elif weather == "cold":
    print("Wear: Jacket and scarf")
else:
    print("Check weather again")