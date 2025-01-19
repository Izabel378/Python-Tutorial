portfolio = [
    {"Asset": "Stock A", "Investment": 1000, "Current Value": 1500},
    {"Asset": "Stock B", "Investment": 2000, "Current Value": 1800},
    {"Asset": "Stock C", "Investment": 1500, "Current Value": 2000},
    {"Asset": "Stock D", "Investment": 2500, "Current Value": 2400},
]
total_investment = 0
total_current_value = 0

print("Investment Portfolio Report")
print("=" * 70)
print(f"{'Asset':<10}{'Investment':>15}{'Current Value':>20}{'Profit/Loss':>15}{'Return (%)':>10}")
print("=" * 70)
for item in portfolio:
    investment = item["Investment"]
    current_value = item["Current Value"]
    profit_loss = current_value - investment
    percentage_return = (profit_loss / investment) * 100
    total_investment += investment
    total_current_value += current_value
    print(f"{item['Asset']:<10}{investment:>15}{current_value:>20}{profit_loss:>15}{percentage_return:>10.2f}")


total_profit_loss = total_current_value - total_investment
overall_percentage_return = (total_profit_loss / total_investment) * 100
print("=" * 70)
print(f"{'TOTAL':<10}{total_investment:>15}{total_current_value:>20}{total_profit_loss:>15}{overall_percentage_return:>10.2f}")
