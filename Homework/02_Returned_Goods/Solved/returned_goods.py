"""Returned Goods."""


# Define a new function called process_claims
def process_claims(claims):
    # Create a variable called `total_claims`, that is the sum of all claims
    total_claims = sum(claims)
    # Calculate a total payout, which is 30% of total_claims:
    total_payout = total_claims * 0.30
    # Return only the total_payout amount
    return total_payout


# Copy and pasting the list of weekly claims:
weekly_claims = [5000, 1000, 8000, 10000, 3000, 3500]

# What's the total insurance payout?
# Use the print() statement to print the returned value from the function.
total_insurance_payout = process_claims(weekly_claims)
print("The total insurance payout is: ", total_insurance_payout)
