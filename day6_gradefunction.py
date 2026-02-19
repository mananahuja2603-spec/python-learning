def grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=00:
        return "D"
    else:
        return "F"
    
a=int(input("Score: "))
print("Grade: ",grade(a))