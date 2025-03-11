

def payingDebtOff( balance,annualInterestRate,monthlyPaymentRate):
    '''
    balance: int, the total cash
    annualInterestRate: float
    monthlyPaymentRate: float

    return: float, the total annual remaining balance
    
    '''
   
    Monthly_Interest_Rate=annualInterestRate/12.0
    
    for months in range (12):
        Minimum_monthly_payment = monthlyPaymentRate * balance  # Minimum payment for the month
        Monthly_unpaid_balance = balance -   Minimum_monthly_payment  # Unpaid balance after payment
        balance = Monthly_unpaid_balance + (Monthly_Interest_Rate * Monthly_unpaid_balance)  # Update balance with interest
    
    return round(balance, 2)  # Round to 2 decimal places

# Test case
print(payingDebtOff(42, 0.2, 0.04)) 

   

    