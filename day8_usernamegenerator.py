first=input("First name: ").lower()
last=input("Last name: ").lower()
age=input("Age: ")
username=first[0]+last+age
print("Your username:", username)
print("Username length", len(username))