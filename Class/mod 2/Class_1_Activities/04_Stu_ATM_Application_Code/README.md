# ATM Application Code

In this activity, you will write the business logic an code associated with 3 ATM functions.


## Instructions

Using the starter code found in the `atm.py` file located in this Unsolved folder, design business logic and then write the code for the following ATM functions:

* Check the account balance.
* Make a deposit.
* Make a withdrawal.

Before you start to write any code, think through the business logic associated with each function. These should include any expected input parameters, validations, and the return value of the function.

Once your business logic is in place, write the associated code for each function.

Use the following business logic and code associated with the `login` function as an example.

```python
# Create the `login` function for the ATM application.
# The login function will take in a user PIN.
# The function should validate the PIN against this list of `accounts`.
# If the PIN is validated, the function should return the account's balance.

def login(pin):
    for account in accounts:
        if int(pin) == account["pin"]:
            account_balance = account['balance']
    return account_balance
```

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
