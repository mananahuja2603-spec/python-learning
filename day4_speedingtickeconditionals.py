speed = int(input("Speed (km/h): "))
limit = 50
if speed > limit + 20:
    print("Heavy fine: £150")
elif speed > limit:
    print("Fine: £50")
else:
    print("Safe driving")