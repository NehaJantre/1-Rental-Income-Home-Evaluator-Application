"""This is a basic ATM Application.

This is a command line application that mimics the actions of an ATM.

Example:
    $ python app.py
"""

import csv
import sys
import fire
import questionary
from pathlib import Path


def load_accounts():
    """Writes account information from CSV to list."""
    csvpath = Path('data/accounts.csv')
    accounts = []
    with open(csvpath, newline='') as csvfile:
        rows = csv.reader(csvfile)
        header = next(rows)
        for row in rows:
            pin = int(row[0])
            balance = float(row[1])
            account = {
                "pin": pin,
                "balance": balance
            }
            accounts.append(account)
        return accounts


def validate_pin(pin):
    """Verifies that PIN is 6 digits long."""

    # Verifies length of pin is 6 digits prints validations message and return True. Else returns False.
    if len(pin) == 6:
        print(f"Your PIN is valid")
        return True
    else:
        return False


def login():
    """Login to the ATM using an account PIN."""

    # Initial CLI asking user to input PIN
    pin = questionary.text("Please enter your 6 digit PIN number:").ask()

    # Calls validate_pin() function to confirm length.
    if not validate_pin(pin):
        sys.exit("Sorry, your account PIN is not valid. It must be 6 digits in length.")

    # If pin validates, calls load_accounts() and then verifies pin against accounts list. Returns account that matches pin.
    accounts = load_accounts()

    for account in accounts:
        if int(pin) == account["pin"]:
            return account

    # If no account was returned above, exit with an error
    sys.exit(
        "Sorry, your login was not successful. Your PIN does not link to an account. Please check your PIN and try again."
    )


def main_menu():
    """Dialog for the ATM Main Menu."""

    # Determines action taken by application.
    action = questionary.select(
        "Would you like to check your balance, make a deposit or make a withdrawal?",
        choices=["check balance", "deposit", "withdrawal"],
    ).ask()
    return action


def make_deposit(account):
    """Deposit Dialog.

        This application captures the deposit amount from the user, validates the amount,
        adjusts the account balance for the deposit and returns the adjusted account.

        Args:
            account(dict): user account information including pin and balance.

        Return:
            account(dict): user account with balance adjusted for deposit

    """
    # Use questionary to capture the deposit and set equal to amount variable. Set amount as a floating point number.
    amount = questionary.text("How much would you like to deposit?").ask()
    amount = float(amount)

    # Validates amount of deposit. If true processes deposit, else returns error.
    if amount > 0.0:
        account["balance"] = account["balance"] + amount
        print(f"Your deposit was successful.")
        return account
    else:
        sys.exit(f"This is not a valid deposit amount. Please try again.")


def make_withdrawal(account):
    """Withdrawal Dialog.

        This application captures the withdrawal amount from the user,
        validates the amount, that their are enough funds in the account,
        adjusts the account balance for the withdrawal and returns the adjusted account.

        Args:
            account(dict): user account information including pin and balance.

        Return:
            account(dict): user account with balance adjusted for deposit

    """
    # Use questionary to capture the withdrawal and set equal to amount variable. Be sure to set amount as a floating point number.
    amount = questionary.text("How much would you like to withdraw?").ask()
    amount = float(amount)

    # Validates amount of withdrawal. If less than or equal to 0 system exits with error message.
    if amount <= 0.0:
        sys.exit("This is not a valid withdrawal amount. Please try again.")

    # Validates if withdrawal amount is less than or equal to account balance, processes withdrawal and returns account.
    # Else system exits with error messages indicating that the account is short of funds.
    if amount <= account["balance"]:
        account["balance"] = account["balance"] - amount
        print("Your withdrawal was successful!")
        return account
    else:
        sys.exit(
            "You do not have enough money in your account to make this withdrawal. Please try again."
        )


def run():
    """The main function for running the script."""

    # Initiates login process. If pin verified, returns validated account.
    account = login()

    # Initiates ATM action: check balance, deposit or withdrawal.
    action = main_menu()

    # Processes the chosen action
    if action == "check balance":
        sys.exit(f"Your current account balance is {account['balance']}")
    elif action == "deposit":
        account = make_deposit(account)
    else:
        account = make_withdrawal(account)

    # Prints the adjusted balance.
    print(
        f"Thank you for your {action}. Your adjusted balance is ${account['balance']: .2f}."
    )

    # @TODO: As a bonus, try writing the adjusted account balance back to the CSV file.


# Entry point for the application. Initiates the run() function.
if __name__ == "__main__":
    fire.Fire(run)
