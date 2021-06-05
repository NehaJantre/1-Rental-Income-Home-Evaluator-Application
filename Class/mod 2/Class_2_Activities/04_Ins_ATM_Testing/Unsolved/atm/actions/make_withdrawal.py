"""Adjusts account balance for withdrawal.

    Script that verifies withdrawal amount is valid, confirms that withdrawal amount is less than account balance, and adjusts account balance.

    Arg:
        account(dict): contains pin and balance for account

    Return:
        account(dict): returns account with balance adjusted for withdrawal

"""

import sys
import questionary


def make_withdrawal(account):
    """Withdrawal Dialog."""
    #
    amount = questionary.text("How much would you like to withdraw?").ask()
    amount = float(amount)

    # Validates amount of withdrawal.
    if amount <= 0.0:
        sys.exit("This is not a valid withdrawal amount. Please try again.")

    # If withdrawal amount is less then account balance, processes withdrawal. Else returns error.
    if amount <= account["balance"]:
        account["balance"] = account["balance"] - amount
        print("Your withdrawal was successful!")
        return account
    else:
        sys.exit(
            "You do not have enough money in your account to make this withdrawal. Please try again."
        )
