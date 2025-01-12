def calculate_income_tax(income):
    """
    Calculate income tax based on simplified tax slabs.
    """
    if income <= 250000:
        return 0
    elif income <= 500000:
        return (income - 250000) * 0.05
    elif income <= 1000000:
        return (250000 * 0.05) + (income - 500000) * 0.1
    else:
        return (250000 * 0.05) + (500000 * 0.1) + (income - 1000000) * 0.2


# Input: User's income
try:
    income = float(input("Enter your annual income: "))
    if income <= 0:
        print("Income must be a positive number.")
    else:
        tax = calculate_income_tax(income)
        print(f"Your income tax is: ₹{tax:.2f}")
except ValueError:
    print("Please enter a valid numeric value for income.")
