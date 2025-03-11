



def payingDebtOff(balance, annualInterestRate):
    '''
    balance: int, the total debt
    annualInterestRate: float, yearly interest rate
    
    returns: int, the lowest fixed monthly payment to pay off debt in 12 months
    '''
    Monthly_Interest_Rate = annualInterestRate / 12.0  # Convert annual rate to monthly
    Minimum_fixed_monthly_payment = 10  # Start from the lowest multiple of 10
    
    while True:  # Keep increasing payment until debt is paid off in 12 months
        test_balance = balance  # Copy of balance for testing payment
        
        # Simulate 12 months of payments
        for month in range(12):
            Monthly_unpaid_balance = test_balance - Minimum_fixed_monthly_payment  # Unpaid balance after payment
            test_balance = Monthly_unpaid_balance + (Monthly_Interest_Rate * Monthly_unpaid_balance)  # Apply interest

        # If balance is paid off (0 or less), return the payment
        if test_balance <= 0:
            break
        
        # Otherwise, increase the payment and try again
        Minimum_fixed_monthly_payment += 10

    return Minimum_fixed_monthly_payment  # Return the lowest possible payment

# Test case
print("Lowest Payment:", payingDebtOff(3329, 0.2))  # Expected Output: 310

   

    