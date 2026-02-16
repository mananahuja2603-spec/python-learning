num1=float(input("First number: "))
num2=float(input("Second number: "))
op=input("Operation (+,-,*,/): ")
if op=="+":
    result=num1+num2
    print("Result: {}".format(result))
elif op=="-":
    result=num1-num2
    print("Result: {}".format(result))
elif op == "*":
    result = num1 * num2
    print("Result: {}".format(result))
elif op=="/":
    if num2!=0:
        result=num1/num2
        print("Result: {}".format(result))
    else:
        print("Cannot Divide By Zero")
else:
    print("Invalid Operation")