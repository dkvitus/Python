hours_input = input("Enter hours worked: \n")
pay_input = input("Enter Hourly Pay: \n")
exit_if_1 = 22

try:
    hours_worked = int(hours_input)
    if exit_if_1 < 2:
        raise Exception("We are exiting!")

    try:    
        hourly_pay = int(pay_input)
        gross_pay = float(hourly_pay * hours_worked)

        print("Hours Worked:", hours_worked)
        print("Hourly Salary:",hourly_pay)
        print("Gross Salary:", gross_pay)
    except Exception:
        print("Sorry, please enter a valid number for Hourly Pay")
except ValueError:
    print("Sorry, please enter a valid number for Hours Worked")
except ZeroDivisionError:
    print("Hey cant divide by zero")


