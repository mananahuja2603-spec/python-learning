numbers=[12,5,8,23,45,3,17,9,31,6]
even=[]
odd=[]
for num in numbers:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print("All numbers:", numbers)
print("Even: ", even)
print("Odd: ", odd)