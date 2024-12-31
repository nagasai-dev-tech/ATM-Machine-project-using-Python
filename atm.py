def atm_machine():
    login_username = "admin"
    login_password = "password123"

    balance = 1000  
    attempts = 5 
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == login_username and password == login_password:
            print("Login successful!")
            while True:
                print("\nATM Menu:")
                print("1. Check Balance")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    print("Your balance is:", balance)
                elif choice == "2":
                    amount = float(input("Enter amount to withdraw: "))
                    if amount > 0 and amount <= balance:
                        balance -= amount
                        print("Withdrawal successful. Your new balance is:", balance)
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                elif choice == "3":
                    amount = float(input("Enter amount to deposit: "))
                    if amount > 0 :
                        balance += amount
                        print("Deposit successful. Your new balance is:", balance)
                    else:
                        print("Invalid deposit amount.")
                elif choice == "4":
                    print("Thank you for using the ATM!")
                    return  
                else:
                    print("Invalid choice. Please try again.")
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Login failed. You have {attempts} attempts remaining.")
            else:
                print("Login failed. Account locked.")
                return 

atm_machine()