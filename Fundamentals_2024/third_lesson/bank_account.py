# Вложени листи
# Примерно създаваш потребител иван
# Апендваш го към лист и става с индекс 1
# После за баланси трябва да създадеш вложен лист във балансите
# И вече в този лист да заложиш баланса на на иван
# Така е и с транзакциите и с заемите
# По принцип в зависимост как го направиш може и без вложени в балансите и заемите
# Но е по чисто според мен
# Но транзакцията е със сигурност със вложен лист
# Initialize lists to hold account data
account_holders = []  # List to store account holder names
balances = []  # List to store corresponding balances
transaction_histories = []  # List to store transaction histories
loans = []  # List to store outstanding loans for each account

MAX_LOAN_AMOUNT = 10000  # Maximum loan amount
INTEREST_RATE = 0.03  # Interest rate for loans


def create_account():
    """Create a new bank account."""

    # 1. Prompt the user for the account holder's name.

    username = input("Enter the account holder's name: ")

    print()

    # 2. Add the new account holder to the list of account holders.

    account_holders.append(username)

    # 3. Initialize the balance to 0 for the new account.

    print('Your balance is 0 lv.')

    # 4. Initialize an empty transaction history for the new account.

    print('Your transaction history is empty.')

    # 5. Initialize the outstanding loan amount to 0.

    print('The outstanding amount of the loan is 0 lv.')

    # 6. Notify the user of the successful account creation.

    print()

    print(f'Hello {username}, your account is ready')

    print()


create_account()


def deposit():
    """Deposit money into an account."""

    # 1. Prompt the user for the account holder's name.

    username = input("Enter the account holder's name: ")

    # 2. Check if the account exists in the system.
    # 3. If the account exists, prompt the user for the amount to deposit.

    if username in account_holders:
        deposit_amount = int(input('Enter deposit sum: '))

        deposit_money = 0

        print()

        # 4. Update the account's balance with the deposited amount.

        balances.append(deposit_amount)

        deposit_money += deposit_amount

        # 5. Log the transaction in the account's transaction history.

        transaction_histories.append(deposit_amount)

        # 6. Display the updated balance to the user.

        print(f'Your balance has been updated. \n'
              f'Your balance is: {deposit_money} lv \n'
              f'Your transaction history is: {transaction_histories} lv.')

        print()

    # 7. If the account does not exist, inform the user.

    elif username not in account_holders:
        print(f'No account with that username, please try again.')

        print()


deposit()


def withdraw():
    """Withdraw money from an account."""

    # 1. Prompt the user for the account holder's name.

    username = input("Enter the account holder's name: ")

    # 2. Check if the account exists in the system.
    # 3. If the account exists, prompt the user for the amount to withdraw.

    if username in account_holders:
        withdrawal_amount = int(input('Enter the amount you want to withdraw: '))

        print()

        # 4. Check if there are sufficient funds for the withdrawal.
        # 5. If funds are sufficient, update the balance and log the transaction.

        if withdrawal_amount <= balances[0]:
            transaction_histories.append(withdrawal_amount)
            balances[0] -= withdrawal_amount

            # 6. Display the updated balance to the user.

            print(f'Your balance has been updated. \n'
                  f'Your balance is: {balances[0]} lv. \n'
                  f'Your transaction history is: {transaction_histories} lv.')

            print()

        # 7. If insufficient funds, inform the user.

        elif withdrawal_amount > balances[0]:
            print('Not enough money.')

            print()

    # 8. If the account does not exist, inform the user.

    elif username not in account_holders:
        print(f'No account with that username, please try again.')

        print()


withdraw()


def check_balance():
    """Check the balance of an account."""

    # 1. Prompt the user for the account holder's name.

    username = input("Enter the account holder's name: ")

    print()

    # 2. Check if the account exists in the system.

    if username in account_holders:
        # 3. If the account exists, display the current balance.

        print(f'Your current balance is: {balances[0]} lv.')

        print()

    # 4. If the account does not exist, inform the user.

    elif username not in account_holders:
        print(f'No account with that username, please try again.')

        print()


check_balance()


def list_accounts():
    """List all accounts and their balances."""

    # 1. Check if there are any accounts in the system.

    # 2. If there are accounts, loop through each account holder.

    if len(account_holders) > 0:

        for account in account_holders:
            print(account)

            # 3. Display the account holder's name, balance, and outstanding loan amount.

            print(f'User is {account_holders[0]} \n'
                  f'Your balance is: {balances} lv. \n'
                  f'Your loan is: {loans} lv.')

            print()

    # 4. If there are no accounts, inform the user.

    else:
        print('There are no registered accounts.')

        print()


list_accounts()


def transfer_funds():
    """Transfer funds between two accounts."""
    # 1. Prompt the user for the sender's and recipient's account holder names.

    username = input("Enter the account holder's name: ")

    print()

    if username in account_holders:
        sender = input('Enter the sender name: ')
        recipient = input('Enter the recipient name: ')

        account_holders.append(recipient)
        account_holders.append(sender)

        # 2. Check if both accounts exist in the system.

        if sender and recipient in account_holders:

            # 3. If both accounts exist, prompt the user for the amount to transfer.

            transfer_amount = int(input('Enter the amount you want to transfer: '))

            print()

            # 4. Check if the sender has sufficient funds for the transfer.
            # 5. If funds are sufficient, update both balances and log the transactions.
            # 6. Inform the user of the successful transfer.

            if balances[0] > transfer_amount:

                transaction = transfer_amount

                transaction_histories.append(transaction)

                balances[0] -= transfer_amount

                print(f'Hello {username} your balance has been updated. \n'
                      f'Your balance is: {balances[0]} lv. \n'
                      f'Your transaction history is: {transaction_histories} lv.')

                print()

                print('Successful transaction.')

                print()

            # 7. If insufficient funds or if either account does not exist, inform the user.

            elif balances[0] < transfer_amount or sender not in account_holders or recipient not in account_holders:
                print("You don't have enough funds or one of the users doesn't exist")

                print()


transfer_funds()


def view_transaction_history():
    """View transaction history for a specific account."""

    # 1. Prompt the user for the account holder's name.

    username = input("Enter the account holder's name: ")

    print()

    # 2. Check if the account exists in the system.
    # 3. If the account exists, display the transaction history.

    if username in account_holders:
        print(f'This is your transaction history: {transaction_histories} lv.')

    # 4. If there are no transactions, inform the user.

    elif len(transaction_histories) < 0:
        print('No transactions registered.')

    # 5. If the account does not exist, inform the user.

    elif username not in account_holders:
        print(f'No account with that username, please try again.')

    print()


view_transaction_history()


def apply_for_loan():
    """Apply for a loan."""

    name = input("Enter the account holder's name: ")

    # Check if the account exists in the system

    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for the loan amount they wish to apply for

        loan_amount = float(input(f"Enter the loan amount (max {MAX_LOAN_AMOUNT} leva): "))

        # Check if the loan amount is within the limit

        if loan_amount <= MAX_LOAN_AMOUNT:

            # Update balance and loan amount

            balances[index] += loan_amount
            loans[index] += loan_amount * (1 + INTEREST_RATE)  # Calculate total loan with interest

            print(f"Loan of {loan_amount:.2f} leva approved for {name}. New balance: {balances[index]:.2f} leva.")
        else:
            print(f"Loan amount exceeds maximum limit of {MAX_LOAN_AMOUNT} leva.")
    else:
        print("Account not found.")


def repay_loan():
    """Repay a loan."""

    name = input("Enter the account holder's name: ")

    # Check if the account exists in the system

    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for repayment amount

        repayment_amount = float(input(f"Enter repayment amount (Outstanding loan: {loans[index]:.2f} leva): "))

        # Check if the repayment amount is valid

        if repayment_amount <= loans[index]:

            # Update balance and outstanding loan amount

            balances[index] -= repayment_amount
            loans[index] -= repayment_amount

            print(
                f"Repayment of {repayment_amount:.2f} leva accepted for {name}. Remaining loan: {loans[index]:.2f} leva.")
        else:
            print("Repayment amount exceeds outstanding loan.")
    else:
        print("Account not found.")


def display_menu():
    """Display the main menu."""
    print("\n--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Transfer Funds")
    print("7. View Transaction History")
    print("8. Apply for Loan")
    print("9. Repay Loan")
    print("10. Exit")

    # Prompt user for their choice

    choice = int(input("Enter your choice: "))
    return choice


display_menu()


def main():
    """Main function to run the banking system."""

    while True:
        choice = display_menu()  # Display the menu and get user choice

        # Process user input based on their choice

        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")


main()


