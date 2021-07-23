#Link: https://replit.com/@appbrewery/tip-calculator-start

print("Welcome to the tip calculator")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10,12, or 15?"))
per=int(input("How many people to split?"))
bill+=bill*(tip/100)
bill=bill/per
bill=round(bill,2)
print(f"Each person should pay: ${bill}")
