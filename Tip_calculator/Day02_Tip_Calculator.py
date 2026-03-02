print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10,12, 0r 15?"))
splitting=int(input("How many people to split the bill?"))
total_tip_amount=total_bill*(tip/100)
total_bill_with_tip=total_bill+total_tip_amount
ans=total_bill_with_tip/splitting
print(f"Each person should pay: ${round(ans,2)}")
