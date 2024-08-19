tempBal = 456.12  # Global variable for balance
temppin = "1234"  # Global variable for the PIN (initial value)

def viewbankbalance():
    global tempBal
    print("Your balance is £", tempBal)

def cashwithdrawal():
    global tempBal
    amount = float(input("Enter the withdrawal amount: £"))
    if amount > tempBal:
        print("Insufficient funds.")
    else:
        tempBal -= amount
        print("Your new bank balance is £", tempBal)

def changepinnumber():
    global temppin
    newpin = input("Enter your new PIN: ")
    temppin = newpin
    print("New PIN number is confirmed.")
    print("Your new PIN number is", newpin)

def enteracheque():
    # Placeholder for entering a cheque
    print("Enter a cheque functionality is not implemented yet.")

def mainMenu():
    while True:
        print("+-----------------------------------------+")
        print("|    WELCOME TO MY BANKING APP            |")
        print("|    Choose an option:                    |")
        print("|     1   View bank balance               |")
        print("|     2   Cash withdrawal                 |")
        print("|     3   Enter a cheque                  |")
        print("|     4   Change PIN number               |")
        print("+-----------------------------------------+")

        reply = input("Please enter a valid option (1-4): ")
        
        if reply == '1':
            viewbankbalance()
        elif reply == '2':
            cashwithdrawal()
        elif reply == '3':
            enteracheque()
        elif reply == '4':
            changepinnumber()
        else:
            print("Please enter a valid option (1-4)")

        exit_choice = input("Would you like to choose another option? (yes/no): ").lower()
        if exit_choice != 'yes':
            break

# Main program starts here
mainMenu()