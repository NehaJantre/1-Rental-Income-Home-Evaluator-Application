"""Listing Assets."""

# 1. Use the following list, or copy this list to your new python script
bank_loans = [200, 500, 900, 100, 400, 800, 100]

# 2. Create a variable called `number_of_loans`,
# declaring its value to be the length of the list of `bank_loans`.
number_of_loans = len(bank_loans)
print(f"There are {number_of_loans} number of loans.")

# 3. Create a variable called `largest_loan_amount’
# make it equal to the maximum value from the list of `bank_loans`.
largest_loan_amount = max(bank_loans)

# 4. Print the largest loan amount.
print(f"The largest loan amount is ${largest_loan_amount}")
