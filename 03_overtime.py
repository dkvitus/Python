hours_input = input("Enter hours worked \n")
pay_input = input("Enter hourly pay \n")

# User Validation is imperative for user input
if (type(hours_input) != int) or (type(hours_input) != float):
    print("Please enter a number for hours worked")

try:
    hours = int(hours_input)
    pay = int(pay_input)


    #If hours is over 40
    if hours > 40:
        overtime = hours - 40
        regular_pay = pay * 40
        ot_pay = overtime * pay * 1.5

        salary = float(regular_pay  + ot_pay)

        print("Hours: ", hours)
        print("Hourly Pay:", pay)
        print("Salary:", salary)
    else:
        salary = float( hours * pay)

        print("Hours: ", hours)
        print("Hourly Pay:", pay)
        print("Salary:", salary)
except:
    print("Please enter a number ")
