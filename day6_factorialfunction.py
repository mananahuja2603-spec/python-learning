def factorial(a):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result

n=int(input("Enter n: "))
print("Factorial: ",factorial(n))