shopping_spree_charges = [10.10, 20, 50, 900, 72.72]
spending_total = 0.0

for charge in shopping_spree_charges:
    spending_total += charge
    print("Inside loop: $", spending_total)

print("The total spent on my spending spree was $", round(spending_total, 2))