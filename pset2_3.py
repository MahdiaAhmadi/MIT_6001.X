





def payingDebtOff(balance, annualInterestRate):
    '''
    balance: int, the total debt
    annualInterestRate: float, yearly interest rate
    
    returns: int, the lowest fixed monthly payment to pay off debt in 12 months
    '''
    Monthly_Interest_Rate = annualInterestRate / 12.0  # Convert annual rate to monthly
    Monthly_payment_lower_bound = balance / 12
    Monthly_payment_upper_bound = (balance * (1 + Monthly_Interest_Rate)**12) / 12.0
    Minimum_fixed_monthly_payment = (Monthly_payment_lower_bound + Monthly_payment_upper_bound) / 2.0

    epsilon = 0.01   # Precision threshold (we stop when the balance is close to 0)

    while True:  # Keep increasing payment until debt is paid off in 12 months
        test_balance = balance  # Copy of balance for testing payment
        
        # Simulate 12 months of payments
        for month in range(12):
            Monthly_unpaid_balance = test_balance - Minimum_fixed_monthly_payment  # Unpaid balance after payment
            test_balance = Monthly_unpaid_balance + (Monthly_Interest_Rate * Monthly_unpaid_balance)  # Apply interest

        # If balance is paid off (0 or less), return the payment
        if abs(test_balance) < epsilon:
            break
        # Adjust bounds based on remaining balance
        if test_balance > 0:
            # Balance is still positive → Increase payment (move lower bound up)
            Monthly_payment_lower_bound = Minimum_fixed_monthly_payment
        else:
            # Balance is negative → Payment was too high (move upper bound down)
            Monthly_payment_upper_bound = Minimum_fixed_monthly_payment

        # Update payment to midpoint
        Minimum_fixed_monthly_payment = (Monthly_payment_lower_bound + Monthly_payment_upper_bound) / 2.0


    return round(Minimum_fixed_monthly_payment, 2)  # Round to 2 decimal places

# Test case
print("Lowest Payment:", payingDebtOff(320000, 0.2))  # Expected Output: Around 29157.09
   

    