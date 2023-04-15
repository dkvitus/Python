# Get car loan details
amount_owed = float(input("How much is your car loan?"))
apr = float(input("How much is your annual percentage rate?"))
payments = float(input("How much is your monthly payment?"))
months = 24

#Get percentage monthly rate
monthly_interest = apr/12/100

#while amount_owed > 0:
#range(12) starts from 0 to 11
for month in range(months):
    # Calculate interest
    interest_paid = amount_owed * monthly_interest
    amount_owed = amount_owed + interest_paid
    
    # Check if balance is less than payment
    if amount_owed < payments:
        print("The last payment is",amount_owed)
        print("You paid off your loan in",months+1,"monhts")
        break

    
    # Make payment
    amount_owed = amount_owed - payments
    
    # Update month
    #months = months - 1
    
    #Print results
    print("Month #:",month)
    print("Paid:",payments,"including", interest_paid,"interest")
    print("Balance:",amount_owed)
    print("*******************")

print("All done!")
          