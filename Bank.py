def show_blnc(balance):
    print(f"\nYour balance is {balance:.2f}\n")

def deposit(balance):
    amount = input('Enter your deposit amount: ')
    while True:
        if amount.isdigit():
            amount = int(amount)  
            if amount >= 0 :
                break
            else :
                amount = ("Value must be greater than zero: ")
        else :
                amount = input("Please enter a valid number: ")
    
    balance += float(amount)
    print("")
    return balance

def withdraw(balance):
    amount = input('Enter your withdraw amount: ')
    while True:
        if amount.isdigit():
            amount = int(amount)  
            if amount <= balance :
                break
            else :
                amount = ("Value must be greater than zero: ")
        else :
                amount = input("Please enter a valid number: ")
    
    balance -= float(amount)
    print("")
    return balance


balance = 0
is_run = True

while is_run:
    
    print("Banking System".center(26, "*"))
    print("*" * 26)

    print(" 1 - Show Balance ")
    print(" 2 - Deposit ")
    print(" 3 - Withdraw ")
    print(" 4 - Exit\n")

    choice = input("Enter a valid choice: ")

    if choice == '1':
        show_blnc(balance)
    elif choice == '2':
        balance = deposit(balance)
    elif choice == '3':
        balance = withdraw(balance)
    elif choice == '4':
        is_run = False
        print("Thanks for using our Banking System Program!")
    else:
        print("\nNone Valid Choice\n")
