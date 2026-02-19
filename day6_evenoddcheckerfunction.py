def is_even(n):
    return n%2==0

num=int(input("Number: "))
if is_even(num):
    print("Even")
else:
    print("Odd")