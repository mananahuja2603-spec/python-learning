choice=""
while choice!="4":
    print("\n1. View balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice=input("Choose: ")
    if choice=="1":
        print("Balance: $1000")
    elif choice=="2":
        print("Deposit successful")
    elif choice == "3":
        print("Withdraw successful")
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Invalid")