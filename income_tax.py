def calculate_income_tax(income):
    tax = 0
    tax_slabs = [
        (250000, 0.05),  
        (500000, 0.1),   
        (1000000, 0.2),  
        (float('inf'), 0.3)  
    ]
    previous_limit = 0
    for limit, rate in tax_slabs:
        if income > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (income - previous_limit) * rate
            break
    return tax
try:
    income = float(input("Enter your annual income: "))
    if income <= 0:
        print("Income must be a positive number.")
    else:
        tax = calculate_income_tax(income)
        print(f"Your income tax is: ₹{tax:.2f}")
except ValueError:
    print("Please enter a valid numeric value for income.")
