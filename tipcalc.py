print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
calc = (total * (1+ tip / 100)) / people

ans = f"Each person should pay {round(calc,2)}$"
print(ans)