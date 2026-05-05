# --- CONSTANTS ---
MAX_ATTEMPTS = 3
PIN = 4240
MIN_DEPOSIT = 50

# --- STATE ---
bank_balance = 1500

# --- LOGIN ---
attempts = 0

while attempts < MAX_ATTEMPTS:
    pin = int(input("Enter PIN: "))

    if pin == PIN:
        print("\n*** WELCOME TO ATM ***")

        # --- MENU LOOP ---
        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = int(input("Choose option: "))

            if choice == 1:
                print("Current Balance:", bank_balance)

            elif choice == 2:
                amount = int(input("Enter deposit amount: "))

                if amount < MIN_DEPOSIT:
                    print("Minimum deposit is", MIN_DEPOSIT)
                else:
                    bank_balance = bank_balance + amount
                    print("Deposit successful")
                    print("New Balance:", bank_balance)

            elif choice == 3:
                amount = int(input("Enter withdraw amount: "))

                if amount > bank_balance:
                    print("Insufficient balance")
                elif amount <= 0:
                    print("Enter valid amount")
                else:
                    bank_balance = bank_balance - amount
                    print("Withdrawal successful")
                    print("New Balance:", bank_balance)

            elif choice == 4:
                print("Thank you. Visit again.")
                break   # exit menu loop

            else:
                print("Invalid option")

        break   # exit login loop after successful session

    else:
        attempts = attempts + 1
        print("Wrong PIN,", MAX_ATTEMPTS - attempts, "attempts left")

# --- BLOCK ACCOUNT ---
if attempts == MAX_ATTEMPTS:
    print("Account blocked due to too many wrong attempts")