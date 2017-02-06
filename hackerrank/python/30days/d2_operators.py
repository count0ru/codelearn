#https://www.hackerrank.com/challenges/30-operators?h_r=email&unlock_token=175835fa37c9f4e2dc6dbbd90b1bd4691a0a6dc4&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder

meal_cost = float(input().strip())
tip_percent = int(input().strip())
tax_percent = int(input().strip())

tip = meal_cost * float(tip_percent/100)
tax = meal_cost * float(tax_percent/100)
total_cost = round(meal_cost + tip + tax)
print("The total meal cost is {} dollars.".format(total_cost))

